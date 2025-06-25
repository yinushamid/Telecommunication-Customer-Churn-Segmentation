# Telecommunication Customer Churn Segmentation
![Dashboard Preview](./Screenshot.png) <!-- Update this if you rename or relocate the image -->

## Project Overview
In today’s competitive telecom industry, customer churn is a major challenge. This project tackles churn head-on using **customer segmentation**, 
enabling targeted retention strategies based on actual behavior and value.
With over 7,000 customer records from a Telco dataset, I applied clustering techniques in Python and brought the insights to life with an interactive 
**Power BI dashboard**—designed to help stakeholders take fast, data-backed actions.

> **Goal**: Understand *why* customers churn and *who* is most at risk.

## The Story Behind the Segments
Every customer has a story—this project segments those stories into four meaningful customer personas:

| Segment | Segment Name | Description |
|--------|--------------|-------------|
| 0 | Stable Value Seekers | Long-term customers with moderate tenure and low charges. Prefer stable payments and longer contracts. |
| 1 | Premium Loyalists | Most valuable, loyal customers with the longest tenure and highest charges. Love long-term contracts. |
| 2 | Churn-Prone Mid-Termers | Mid-tenure customers with moderate to high charges. Often on month-to-month plans—at risk of churn. |
| 3 | High-Risk New Entrants | Newest customers with high monthly charges and short-term plans. Very likely to churn. |

These segments were discovered using **K-Means Clustering**, based on:
- Tenure
- Payment Method
- Monthly Charges
- Contract Type

##  Tools & Techniques
### Python (Customer Segmentation)
- `Pandas`, `Sklearn`, `Matplotlib`, `Seaborn`
- Data preprocessing, encoding, and scaling
- K-Means clustering with Elbow method optimization
- Segment profiling and churn aggregation

### Power BI (Dashboard & Insights)
- Visual segmentation profiles
- Churn vs. No Churn comparison
- Filters by segment name
- KPI table: tenure, charges, contract & payment type

## Key Insights

- **High-Risk New Entrants** had the **highest churn rate (44%)**, highlighting the need for onboarding-focused retention strategies.
- **Premium Loyalists** showed **over 91% retention**, signaling the importance of long-term plans and customer loyalty programs.
- Segment-based churn analysis gives deeper visibility compared to general averages.

## Key Insights (What the Data Revealed)
This project isn't just about running K-Means clustering—it's about uncovering the **"why"** behind customer behavior. 

These are the most actionable insights that emerged from the segmentation:

### 1. High-Risk New Entrants Are the Most Likely to Churn
- Represent **~22%** of total customers
- Characterized by:
  - Very **short tenure**
  - **High monthly charges**
  - Mostly on **month-to-month contracts**
- **Churn rate:** **44%**

** Business Implication:**  
These customers are in the trial phase and are expensive to retain. They’re highly sensitive to price and experience. Proactive onboarding, 
personalized communication, or flexible contract offers could help convert them into long-term subscribers.

###  2. Premium Loyalists Are the Telco's Power Customers
- Longest tenure and highest monthly charges
- Loyal to **1–2 year contracts**
- **Churn rate:**  **8.55%**

** Business Implication:**  
This is your most profitable and loyal customer group. They require protection through loyalty programs, exclusive upgrades, and premium customer care to maintain retention and maximize lifetime value.

###  3. Churn-Prone Mid-Termers Need Close Monitoring
- Mid-level tenure and moderate-to-high charges
- Mostly prefer **month-to-month contracts**
- **Churn rate:**  **30.63%**
- 
** Business Implication:**  
These users may appear stable but are quietly at risk. They’re indecisive and disengaged—ideal targets for nudges like contract upgrade offers,
targeted campaigns, or retention calls before they churn unnoticed.

### 4. Stable Value Seekers Are Quiet but Reliable
- Prefer **low charges** and **longer-term contracts**
- Moderate tenure, consistent behavior
- **Churn rate:**  **2.13%**

** Business Implication:**  
Often overlooked, this group brings quiet, long-term value with minimal support cost. Consider upselling based on known preferences or offering lightweight 
loyalty incentives to boost ARPU (Average Revenue Per User).

### Strategic Takeaway

Segmented churn analysis is far more insightful than overall churn percentages. It empowers businesses to:

-  Implement **targeted retention strategies** instead of generic campaigns
-  Allocate **budgets more efficiently** based on risk and value
-  Deliver **personalized communications** that resonate with each segment

  ### References
- Dataset: telecommunication Data from Kaggle

> Understanding **who churns** and **why** leads to smarter, more profitable decisions.


