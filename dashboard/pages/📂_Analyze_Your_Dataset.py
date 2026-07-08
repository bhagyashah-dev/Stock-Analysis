import streamlit as st

from utils import (
    load_multiple_data, filter_data, get_dataset_overview, get_company_kpis,
    get_average_close, get_average_volume, get_average_daily_return,
    get_total_return, get_volatility, get_correlation
)
from charts import (
    average_close_chart, average_volume_chart, average_daily_return_chart, 
    total_return_chart, volatility_chart, correlation_heatmap, 
    closing_price_chart, volume_trend_chart, moving_average_chart, 
    daily_return_chart, open_close_chart, volume_close_chart
)

st.set_page_config(page_title="Analyze Your Dataset", page_icon="📂", layout="wide")
st.title("📂 Upload Your Stock Dataset")
st.write(
    """
Upload one or more stock CSV files to generate the same financial analysis,
technical indicators, and interactive visualizations available in the Sensex dashboard.
"""
)
uploaded_files = st.file_uploader(
    "Upload one or more CSV files",
    type=["csv"],
    accept_multiple_files=True
)
st.markdown("""
### Required CSV Format

Each uploaded CSV should contain:

- Date
- Open
- High
- Low
- Close
- Volume
""")

if not uploaded_files:
    st.info("Upload one or more CSV files to begin analysis.")
    st.stop()
with st.spinner("Processing uploaded datasets..."):
    master_df = load_multiple_data(uploaded_files)
st.success(f"Successfully uploaded {len(uploaded_files)} file(s).")

with st.expander("Uploaded Files"):
    for file in uploaded_files:
        st.write(f"📄 {file.name}")
st.info(
    f"Dataset contains {master_df['Stock'].nunique()} companies and "
    f"{len(master_df):,} records."
)

st.sidebar.header("Dashboard Filters")
st.sidebar.divider()
companies=["All Companies"]+sorted(master_df["Stock"].unique())
selected_company=st.sidebar.selectbox("Select Company",companies)
min_date=master_df["Date"].min().date()
max_date=master_df["Date"].max().date()
date_range=st.sidebar.date_input("Select Date Range",value=(min_date,max_date),min_value=min_date,max_value=max_date)

master_df["Daily_Return"] = (master_df.groupby("Stock")["Close"].pct_change() * 100)
master_df["MA20"] = (master_df.groupby("Stock")["Close"].transform(lambda x: x.rolling(20).mean()))
master_df["MA50"] = (master_df.groupby("Stock")["Close"].transform(lambda x: x.rolling(50).mean()))

master_df = master_df.sort_values(["Stock", "Date"]) # Sorting Again
filtered_df=filter_data(master_df,selected_company,date_range)

st.write(f"Showing **{len(filtered_df):,}** records")

col1,col2,col3,col4=st.columns(4)

if selected_company=="All Companies":
    overview=get_dataset_overview(filtered_df)
    col1.metric("Total Companies",overview["total_companies"])
    col2.metric("Total Records",f'{overview["total_records"]:,}')
    col3.metric("Trading Days",overview["trading_days"])
    col4.metric("Years Covered",overview["years_covered"])
    st.caption(f'📅 Date Range: {overview["start_date"]} → {overview["end_date"]}')

    st.header("📊 Market Comparison")
    c1,c2=st.columns(2)
    with c1:
        st.plotly_chart(average_close_chart(get_average_close(filtered_df)),use_container_width=True)
    with c2:
        st.plotly_chart(average_volume_chart(get_average_volume(filtered_df)),use_container_width=True)

    st.header("📈 Performance Analysis")
    c1,c2,c3=st.columns(3)
    with c1:
        st.plotly_chart(average_daily_return_chart(get_average_daily_return(filtered_df)),use_container_width=True)
    with c2:
        st.plotly_chart(total_return_chart(get_total_return(filtered_df)),use_container_width=True)
    with c3:
        st.plotly_chart(volatility_chart(get_volatility(filtered_df)),use_container_width=True)

    st.header("🔍 Correlation Analysis")
    st.plotly_chart(correlation_heatmap(get_correlation(filtered_df)),use_container_width=True)

else:
    kpi=get_company_kpis(filtered_df)
    col1.metric("Latest Close",f'₹{kpi["latest_close"]:,.2f}')
    col2.metric("Highest Close",f'₹{kpi["highest_close"]:,.2f}')
    col3.metric("Lowest Close",f'₹{kpi["lowest_close"]:,.2f}')
    col4.metric("Average Volume",f'{kpi["average_volume"]:,.0f}')

    st.header("📈 Price Analysis")
    c1,c2=st.columns(2)
    with c1:
        st.plotly_chart(closing_price_chart(filtered_df,selected_company),use_container_width=True)
    with c2:
        st.plotly_chart(volume_trend_chart(filtered_df,selected_company),use_container_width=True)

    st.header("📊 Technical Analysis")
    st.plotly_chart(moving_average_chart(filtered_df,selected_company),use_container_width=True)

    st.header("📉 Return Analysis")
    st.plotly_chart(daily_return_chart(filtered_df,selected_company),use_container_width=True)

    st.header("🔍 Relationship Analysis")
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(open_close_chart(filtered_df,selected_company),use_container_width=True)
    with c2:
        st.plotly_chart(volume_close_chart(filtered_df,selected_company),use_container_width=True)

with st.expander("📋 Dataset Explorer"):
    st.dataframe(filtered_df,use_container_width=True)

st.download_button(
    label="Download Filtered Dataset",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_stock_data.csv",
    mime="text/csv"
)