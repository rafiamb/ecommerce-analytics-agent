import os
import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# main page
st.set_page_config(
    page_title="Olist Data Analyst Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("Olist Data Analyst Agent")
st.caption("Ask questions about 100K+ Brazilian e-commerce orders.")

# sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        st.error("App not configured. Owner needs to set OPENAI_API_KEY.")
        st.stop()

    st.markdown("**Example questions:**")
    example_qs = [
        "Which 5 states have the highest late delivery rate?",
        "What is the average review score for late vs on-time orders?",
        "Which product category generates the most revenue?",
        "How many orders were placed each month in 2018?",
        "Which sellers have the best on-time rate with over 50 orders?",
        "What's the average number of days between order and delivery?",
    ]
    for q in example_qs:
        if st.button(q, use_container_width=True):
            st.session_state["prefill"] = q

# initialize database and agent
@st.cache_resource
def load_agent(key: str):
    """load SQL agent once and cache it"""
    db = SQLDatabase.from_uri(
        "sqlite:///olist.db",
        include_tables=[
            "orders", "order_items", "order_reviews",
            "order_payments", "customers", "products",
            "sellers", "category_translation"
        ],
        sample_rows_in_table_info=3, 
    )

    llm = ChatOpenAI(
        model="gpt-4o", 
        api_key=key, 
        temperature=0
    )

    agent = create_sql_agent(
        llm=llm,
        db=db,
        agent_type="openai-tools",
        verbose=False,
        max_iterations=8,
        handle_parsing_errors=True,
    )
    return agent, db


# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "sql" in msg:
            with st.expander("SQL used"):
                st.code(msg["sql"], language="sql")

# input
prefill = st.session_state.pop("prefill", "")
user_input = st.chat_input("Ask a question about the Olist dataset...", key="chat_input")
question = user_input or prefill

if question:
    if not api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
        st.stop()

    if not os.path.exists("olist.db"):
        st.error("olist.db not found. Run notebook.py first to build the database.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                agent, db = load_agent(api_key)

                # capture SQL query used (optional enrichment)
                sql_used = None
                try:
                    # run agent
                    result = agent.invoke({"input": question})
                    answer = result.get("output", str(result))

                    # try to extract SQL from intermediate steps
                    for step in result.get("intermediate_steps", []):
                        if hasattr(step, "__iter__"):
                            for part in step:
                                if hasattr(part, "tool_input") and "SELECT" in str(part.tool_input).upper():
                                    sql_used = str(part.tool_input)
                                    break
                except Exception as e:
                    answer = f"I ran into an issue: {str(e)}\n\nTry rephrasing the question."

                st.markdown(answer)
                if sql_used:
                    with st.expander("🔍 SQL used"):
                        st.code(sql_used, language="sql")

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sql": sql_used or "",
                })

            except Exception as e:
                st.error(f"Agent error: {e}")

# footer
st.markdown("---")
st.caption("Built with LangChain · SQLite · Streamlit  |  Data: Olist Brazilian E-Commerce (Kaggle)")