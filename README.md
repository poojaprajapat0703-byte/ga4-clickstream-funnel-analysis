# GA4 Clickstream Funnel & Sequence Analysis 🚀
## 🔍 Project Overview

This project is an **end-to-end GA4 clickstream funnel analysis application** built using **Python and Streamlit**. It analyzes event-level user interaction data to uncover:
* User journey paths
* Funnel drop-offs
* Conversion behavior
* Time taken between funnel steps
  
The app is designed to simulate **real-world product analytics use cases** commonly handled by Data Analysts and Product/Data Scientists.

## 🎯 Key Objectives

* Understand **how users move through events** (page_view → add_to_cart → purchase)
* Identify **top drop-off points** in funnels
* Analyze **session-level event sequences**
* Measure **conversion rates and time gaps** between events
  
## 🛠️ Tech Stack

* **Python** (Pandas, NumPy)
* **Streamlit** (App & deployment)
* **Matplotlib / Plotly** (Visualizations)
* **GitHub** (Version control)
* **Streamlit Community Cloud** (Deployment)

## 📊 Features

### 1️⃣ Data Loading

* Upload GA4-style event-level CSV data
* Automatic validation and preview

### 2️⃣ Dataset Overview

* Total events
* Unique users
* Unique sessions

### 3️⃣ Exploratory Event Sequences

* Top 10 most common event sequences per session
* Helps understand dominant user paths

### 4️⃣ Funnel Analysis

* Configurable funnel steps
* Session-based funnel construction
* Conversion % at each step

### 5️⃣ Drop-off Analysis

* Identifies **where users exit the funnel**
* Highlights biggest leakage points

### 6️⃣ Time Analysis

* Measures time between consecutive funnel steps
* Useful for UX and performance optimization

### 📁 Repository Structure

ga4-clickstream-funnel-analysis/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── Data/                 # Sample GA4-style datasets
├── Notebooks/            # EDA & analysis notebooks
└── README.md             # Project documentation
```

## 🌐 Live Application

👉 **Deployed App:**
[Click here to open the Streamlit app]:[(https://ga4-clickstream-funnel-analysis-dppqevf5mt8jddrw3gnx9j.streamlit.app)]

## 🧠 Business Use Cases

* Product funnel optimization
* Growth analytics
* UX drop-off diagnosis
* GA4 behavioral analysis
* Conversion rate optimization (CRO)

## 📌 Why This Project Matters

This project demonstrates:

* Real-world GA4 analytics thinking
* Ability to convert raw clickstream data into insights
* End-to-end ownership (analysis → app → deployment)
* Interview-ready analytics storytelling

## 👤 Author

**Pooja Prajapat**
Aspiring Data Analyst / Data Scientist
📍 Bengaluru, India

⭐ If you find this project useful, consider giving it a star!
