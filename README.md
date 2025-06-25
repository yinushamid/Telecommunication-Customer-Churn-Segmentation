# 📊 Telecommunication Customer Churn Segmentation

![Dashboard Preview](./Screenshot.png) <!-- Update this if you rename or relocate the image -->

## 🔍 Project Overview

In today’s competitive telecom industry, customer churn is a major challenge. This project tackles churn head-on using **customer segmentation**, 
enabling targeted retention strategies based on actual behavior and value.

With over 7,000 customer records from a Telco dataset, I applied clustering techniques in Python and brought the insights to life with an interactive 
**Power BI dashboard**—designed to help stakeholders take fast, data-backed actions.

> **Goal**: Understand *why* customers churn and *who* is most at risk.

---

## 🧠 The Story Behind the Segments

Every customer has a story—this project segments those stories into four meaningful customer personas:

| Segment | Segment Name | Description |
|--------|--------------|-------------|
| 0 | Stable Value Seekers | Long-term customers with moderate tenure and low charges. Prefer stable payments and longer contracts. |
| 1 | Premium Loyalists | Most valuable, loyal customers with the longest tenure and highest charges. Love long-term contracts. |
| 2 | Churn-Prone Mid-Termers | Mid-tenure customers with moderate to high charges. Often on month-to-month plans—at risk of churn. |
| 3 | High-Risk New Entrants | Newest customers with high monthly charges and short-term plans. Very likely to churn. |

These segments were discovered using **K-Means Clustering**, based on:
- 📈 Tenure
- 💳 Payment Method
- 💰 Monthly Charges
- 📃 Contract Type

---

## 🛠️ Tools & Techniques

### 📌 Python (Customer Segmentation)
- `Pandas`, `Sklearn`, `Matplotlib`, `Seaborn`
- Data preprocessing, encoding, and scaling
- K-Means clustering with Elbow method optimization
- Segment profiling and churn aggregation

### 📌 Power BI (Dashboard & Insights)
- Visual segmentation profiles
- Churn vs. No Churn comparison
- Filters by segment name
- KPI table: tenure, charges, contract & payment type

---

## 🧾 Key Insights

- 🔥 **High-Risk New Entrants** had the **highest churn rate (44%)**, highlighting the need for onboarding-focused retention strategies.
- 🛡 **Premium Loyalists** showed **over 91% retention**, signaling the importance of long-term plans and customer loyalty programs.
- 📊 Segment-based churn analysis gives deeper visibility compared to general averages.

---

## 📁 Project Structure

