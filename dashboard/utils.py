import pandas as pd


# Load Dataset

import streamlit as st

@st.cache_data
def load_data(filepath="data/Sensex30_Master_Cleaned.csv"):
    df = pd.read_csv(filepath)

    # Data Cleaning
    df.columns = df.columns.str.strip()
    df["Date"] = pd.to_datetime(df["Date"])
    df.sort_values("Date", inplace=True)
    return df


# Apply Filters

def filter_data(df, company, date_range):
    filtered_df = df.copy()

    if company != "All Companies":
        filtered_df = filtered_df[filtered_df["Stock"] == company]

    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[(filtered_df["Date"] >= pd.to_datetime(start_date))&(filtered_df["Date"] <= pd.to_datetime(end_date))]

    return filtered_df


# Dataset Overview KPIs

def get_dataset_overview(df):
    return {
        "total_companies": df["Stock"].nunique(), 
        "total_records": len(df), 
        "trading_days": df["Date"].nunique(), 
        "years_covered": round((df["Date"].max()-df["Date"].min()).days / 365, 1), 
        "start_date": df["Date"].min().date(), 
        "end_date": df["Date"].max().date()
    }


# Company KPIs

def get_company_kpis(df):
    return {
        "latest_close": df["Close"].iloc[-1], 
        "highest_close": df["Close"].max(), 
        "lowest_close": df["Close"].min(), 
        "average_volume": df["Volume"].mean()
    }


# Average Closing Price

def get_average_close(df):
    return (
        df.groupby("Stock", as_index=False)["Close"].mean().sort_values("Close", ascending=False)
    )


# Average Trading Volume

def get_average_volume(df):
    return (
        df.groupby("Stock", as_index=False)["Volume"].mean().sort_values("Volume", ascending=False)
    )


# Average Daily Return

def get_average_daily_return(df):
    return (
        df.groupby("Stock", as_index=False)["Daily_Return"].mean().sort_values("Daily_Return", ascending=False)
    )


# Total Return

def get_total_return(df):
    performance = (
        df.groupby("Stock").agg(First_Close=("Close", "first"), Last_Close=("Close", "last"))
    )

    performance["Total_Return"] = ((performance["Last_Close"]-performance["First_Close"])/performance["First_Close"]) * 100
    performance.reset_index(inplace=True) #since stock is an index (as_index=False not written) 
    performance.sort_values("Total_Return", ascending=False, inplace=True)
    return performance


# Volatility

def get_volatility(df):
    volatility = (
        df.groupby("Stock", as_index=False)["Daily_Return"].std()
    )

    volatility.rename(columns={"Daily_Return": "Volatility"}, inplace=True)
    volatility.sort_values("Volatility", ascending=False, inplace=True)
    return volatility


# Correlation Matrix

def get_correlation(df):
    close_prices = df.pivot(index="Date", columns="Stock", values="Close")
    return close_prices.corr()