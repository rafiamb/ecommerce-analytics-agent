# Olist Data Analyst Agent

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=white)

A conversational AI agent that lets you query 100,000+ Brazilian e-commerce orders in plain English — no SQL required.

Built to explore LLM-powered data analysis and natural language interfaces for SQL databases. The agent takes a plain-English question, generates the appropriate SQL query, executes it against a real e-commerce dataset, and returns a natural language answer with the option to inspect the SQL it used.

---

## Demo

🔗 **Live Demo: [olist-agent.streamlit.app](https://olist-agent.streamlit.app/)**

---

## What It Does

Type a question in plain English and the agent writes and executes SQL against the Olist dataset, then returns a natural language answer. You can also expand the response to see the exact SQL it ran.

**Example questions you can ask:**
- Which 5 states have the highest late delivery rate?
- What is the average review score for late vs on-time orders?
- Which product category generates the most revenue?
- How many orders were placed each month in 2018?
- Which sellers have the best on-time rate with over 50 orders?
- What's the average number of days between order and delivery?

---

## Tech Stack

| Layer | Tool |
|---|---|
| Frontend | Streamlit |
| Agent | LangChain SQL Agent |
| LLM | GPT-4o (OpenAI) |
| Database | SQLite (`olist.db`) |
| Data | [Olist Brazilian E-Commerce — Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |

---

## Running Locally

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your OpenAI API key**

Create a `.env` file in the project root:
```
OPENAI_API_KEY=sk-...
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## Project Structure

```
├── app.py               # Main Streamlit app
├── olist.db             # SQLite database (built from Olist dataset)
├── requirements.txt     # Python dependencies
├── .env                 # API keys (not committed)
└── README.md
```

---

## Dataset

The [Olist dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) contains ~100,000 orders made at Olist Store between 2016 and 2018 across multiple marketplaces in Brazil. It includes order status, pricing, payment, freight performance, customer location, product attributes, and customer reviews.

Tables used: `orders`, `order_items`, `order_reviews`, `order_payments`, `customers`, `products`, `sellers`, `category_translation`.

---

## Deployment

Deployed on [Streamlit Community Cloud](https://streamlit.io/cloud). To deploy your own instance:

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Add `OPENAI_API_KEY` under **Advanced settings → Secrets**
4. Click **Deploy**

---

## License
This project is licensed under the MIT License.
