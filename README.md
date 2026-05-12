# E-Commerce Analytics Agent

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=white)

A conversational AI agent that lets you query 100,000+ Brazilian e-commerce orders in plain English. No SQL required.

🔗 **Live Demo: [olist-agent.streamlit.app](https://olist-agent.streamlit.app/)** *(may take ~30 seconds to wake up on first load)*

---

## Project Background

Built on the [Olist Brazilian E-Commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (~100,000 orders across 8 relational tables spanning 2016–2018), this project started as an exploratory analysis of delivery performance and its impact on customer satisfaction — then extended into a conversational AI layer to make those insights accessible without SQL.

The EDA revealed a clear, measurable relationship between logistics performance and customer reviews. Those findings shaped the agent's design: the example queries and schema context are specifically tuned to surface delivery patterns, seller reliability, and category-level performance.

The full EDA notebook covering late delivery rates, review score impact, delay distributions, category revenue, and seller reliability is [here](https://github.com/rafiamb/ecommerce-analytics-agent/blob/main/olist_ecom_eda.ipynb).

---

## Key Findings

| # | Finding |
|---|---------|
| 1 | ~8% of delivered orders arrive late, concentrated in northern/remote states |
| 2 | Late orders score ~2 points lower on average (out of 5) — a direct, measurable cost |
| 3 | Most delays are 1–5 days, but a long tail of 30+ day delays drives disproportionate review damage |
| 4 | Health & beauty and watches/gifts generate the most revenue — high-stakes categories for on-time delivery |
| 5 | Revenue ≠ reliability: top sellers vary widely in on-time rates |

**Recommendations:**
- **Prioritize carrier coverage in high-delay states** — targeted SLA negotiations or regional carrier partnerships could meaningfully reduce late rates in underserved areas
- **Introduce seller reliability scores** — surface on-time rate alongside revenue in seller dashboards to incentivize accountability
- **Flag extreme-delay risk orders early** — orders with long estimated delivery windows are more likely to breach SLA; proactive communication can soften review impact

---

## How It Works

The agent accepts natural language questions, generates the appropriate SQL query, executes it against the Olist database, and returns a natural language answer. Users can expand any response to inspect the underlying SQL that was run.

![Agent Demo](ecom_agent.png)

**Example questions:**

- Which 5 states have the highest late delivery rate?
- What is the average review score for late vs on-time orders?
- Which product category generates the most revenue?
- How many orders were placed each month in 2018?
- Which sellers have the best on-time rate with over 50 orders?
- What's the average number of days between order and delivery?
- What's the review score distribution for orders delayed 7+ days?
- Which states have both high revenue and high late delivery rates?

---

## Tech Stack

| Layer | Tool |
|-------|------|
| Frontend | Streamlit |
| Agent | LangChain SQL Agent |
| LLM | GPT-4o (OpenAI) |
| Database | SQLite (`olist.db`) |
| Data | [Olist Brazilian E-Commerce — Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |

---

## Data Structure

The Olist dataset contains ~100,000 orders made across multiple marketplaces in Brazil, covering order status, pricing, payment, freight performance, customer location, product attributes, and customer reviews.

Tables used: `orders`, `order_items`, `order_reviews`, `order_payments`, `customers`, `products`, `sellers`, `category_translation`.

---

## Running Locally

**1. Clone the repo**
```
git clone https://github.com/rafiamb/ecommerce-analytics-agent.git
cd ecommerce-analytics-agent
```

**2. Install dependencies**
```
pip install -r requirements.txt
```

**3. Add your OpenAI API key**

Create a `.env` file in the project root:
```
OPENAI_API_KEY=sk-...
```

**4. Run the app**
```
streamlit run app.py
```

---

## Project Structure

```
├── app.py               # Main Streamlit app
├── olist_ecom_eda.ipynb # EDA notebook: delivery performance, category revenue, seller reliability
├── olist.db             # SQLite database (built from Olist dataset)
├── requirements.txt     # Python dependencies
├── .env                 # API keys (not committed)
└── README.md
```

---

## Deployment

Deployed on [Streamlit Community Cloud](https://streamlit.io/cloud). To deploy your own instance:

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Add `OPENAI_API_KEY` under **Advanced settings → Secrets**
4. Click **Deploy**

---

## License

MIT License
