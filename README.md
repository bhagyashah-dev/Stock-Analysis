# 📈 Sensex 30 Stock Market Analytics Dashboard

An end-to-end data analytics project that explores the historical performance of the Top 30 S&P BSE Sensex companies using Python, Exploratory Data Analysis (EDA), and an interactive Streamlit dashboard.

The project covers the complete analytics workflow—from collecting and preprocessing stock market data to engineering financial features, performing statistical analysis, and developing an interactive dashboard for data exploration.

---

## 📌 Project Overview

This project analyzes approximately **21,700+ historical stock market records** of the Top 30 Sensex companies over a period of nearly **3 years**.

The objective is to understand stock performance through statistical analysis, financial metrics, correlation analysis, volatility analysis, and interactive visualizations.

---

## 🚀 Features

### 📊 Exploratory Data Analysis (EDA)

- Dataset overview and preprocessing
- Missing value and duplicate analysis
- Feature engineering
- Univariate analysis
- Bivariate analysis
- Time-series analysis
- Correlation analysis
- Stock performance analysis
- Volatility analysis
- Moving Average analysis

---

### ⚙️ Financial Features Engineered

The following financial features were created during preprocessing:

- Daily Return (%)
- 20-Day Moving Average (MA20)
- 50-Day Moving Average (MA50)
- Total Return (%)

---

### 📈 Interactive Streamlit Dashboard

#### 🌍 All Companies Dashboard

- Dataset Overview
    - Total Companies
    - Total Records
    - Trading Days
    - Years Covered

- Market Comparison
    - Average Closing Price
    - Average Trading Volume

- Performance Analysis
    - Average Daily Return
    - Total Return
    - Stock Volatility

- Correlation Heatmap

---

#### 🏢 Company-wise Dashboard

- Latest Closing Price
- Highest Closing Price
- Lowest Closing Price
- Average Trading Volume

##### Price Analysis

- Closing Price Trend
- Trading Volume Trend

##### Technical Analysis

- 20-Day & 50-Day Moving Average

##### Return Analysis

- Daily Return Trend

##### Relationship Analysis

- Open Price vs Closing Price
- Trading Volume vs Closing Price

##### Dataset Explorer

- Interactive filtered dataset

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit

---

## 📷 Dashboard Preview

### 📈 All Companies Dashboard & Analysis

<p align="center">
  <a href="assets/dashboard%20(1).png">
    <img src="assets/dashboard%20(1).png" width="48%">
  </a>

  <a href="assets/dashboard%20(2).png">
    <img src="assets/dashboard%20(2).png" width="48%">
  </a>
</p>

### 📊 Individual Company Dashboard & Analysis

<p align="center">
  <a href="assets/dashboard%20(3).png">
    <img src="assets/dashboard%20(3).png" width="48%">
  </a>

  <a href="assets/dashboard%20(4).png">
    <img src="assets/dashboard%20(4).png" width="48%">
  </a>
</p>

### 🔍 Relationship Analysis

<p align="center">
  <a href="assets/dashboard%20(5).png">
    <img src="assets/dashboard%20(5).png" width="90%">
  </a>
</p>

---

## 📂 Project Structure

```
Stock Analysis/
│
├── dashboard/
│   ├── app.py
│   ├── charts.py
│   ├── utils.py
│
├── notebooks/
│   └── EDA.ipynb
│
├── data/
│   └── Sensex30_Master_Cleaned.csv
│
├── requirements.txt
│
└── README.md
```

---

## 📊 Key Analysis Performed

- Historical stock price analysis
- Trading volume analysis
- Daily return analysis
- Total return comparison
- Volatility comparison
- Correlation analysis
- Moving Average trend analysis
- Company-wise performance comparison

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

Move into the project directory

```bash
cd your-repository-name
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run dashboard/app.py
```

## 📈 Future Improvements

- Portfolio performance analysis
- Candlestick charts
- Risk-adjusted return metrics
- Company comparison dashboard
- Live stock price integration
- Dashboard deployment

---

This Project was built during Summer Internship at Elite TechnoCrats.

## 👨‍💻 Author

**Bhagya Shah**

Computer Science & Business Systems (CSBS) Undergraduate

Passionate about Data Analytics, Backend Development, and Full Stack Development.

---

## ⭐ If you found this project helpful, consider giving it a star!