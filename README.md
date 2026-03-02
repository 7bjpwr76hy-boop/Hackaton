# Hackaton
Global Relocation Engine
🌍 Global Relocation & Travel Decision Intelligence Engine
📌 Overview

The Global Relocation & Travel Decision Intelligence Engine is a full-stack decision-support system that compares multiple countries and provides ranked, explainable recommendations for relocation or travel.

Instead of manually checking weather, healthcare, and environmental data across different platforms, this system aggregates real-time public data, normalizes it, computes intelligence scores, and generates context-aware rankings based on user preferences.

🎯 Objective

Users provide:

A list of at least three countries

Risk tolerance (Low / Moderate / High)

Duration (Short-term / Long-term)

The system:

Fetches real-time data from multiple public APIs

Normalizes heterogeneous metrics to a 0–100 scale

Computes derived intelligence scores

Applies dynamic weighting based on user input

Ranks countries from most suitable to least suitable

Returns structured and explainable JSON results

🔗 Public APIs Used

The backend integrates real public APIs (no mock data):

Country Profile API → Capital, Population, Currency

World Bank API → Life Expectancy, Healthcare Expenditure

Weather API → Current Temperature

AQI API → Air Quality Index

All raw responses are cleaned and structured before scoring.

📊 Intelligence Scores

Each country receives three derived scores:

1️⃣ Travel Risk Score (0–100)

Based on:

Temperature deviation

AQI severity

Risk indicators

2️⃣ Health Infrastructure Score (0–100)

Based on:

Life expectancy

Healthcare expenditure

3️⃣ Environmental Stability Score (0–100)

Based on:

AQI levels

Environmental conditions

All metrics are normalized before aggregation.

⚖ Dynamic Weighting

Scoring weights change depending on:

Risk Tolerance

Low → Higher environmental penalties

High → Lower penalties

Duration

Long-term → Greater weight on healthcare

Short-term → Greater weight on environmental conditions

This ensures personalized, context-aware ranking.

🏆 Ranking & Explainability

Countries are sorted by overall score

Each result includes:

Score breakdown

Overall score

Structured reasoning

Example reasoning:

High air pollution reduced environmental score.
Strong healthcare indicators improved ranking.

⚡ Performance & Concurrency

Uses asynchronous API calls (asyncio.gather)

Avoids blocking requests

Designed to respond under 2 seconds for 3-country analysis

🛡 Resilience

Handles partial API failures

Returns structured error messages

Never crashes due to third-party instability

📂 Project Structure
global_engine_backend/
│
├── server.py
├── models/
├── services/
└── scoring/

Modular separation ensures scalability and maintainability.

🚀 How to Run

Install dependencies:

pip install fastapi uvicorn httpx python-dotenv

Add API keys in .env:

OPENWEATHER_API_KEY=your_key
AQICN_API_KEY=your_key

Start server:

python -m uvicorn server:app --reload

Open:

http://1**.*.*.*:8***/docs
✅ Key Features

✔ Real-time multi-source data integration
✔ Metric normalization
✔ Dynamic multi-factor scoring
✔ Context-aware weighting
✔ Explainable ranking
✔ Async backend architecture

📌 Conclusion

This project demonstrates how fragmented global public data can be transformed into structured, comparable, and explainable intelligence for smarter relocation and travel decisions.
