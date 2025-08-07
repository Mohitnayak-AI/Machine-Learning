import streamlit as st
from datetime import date
import requests

import pandas as pd

API_URL = "http://localhost:8000"

def analytics_tab():
    col1,col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", date(2024,8,1))
    with col2:
        end_date = st.date_input("End Date",date(2024,8,5))
    if st.button("Analysis"):
        payload ={
            "start_date":start_date.strftime("%Y-%m-%d"),
            "end_date":end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics/",json=payload)
        if response.status_code == 200:
            response = response.json()
            data = {
                "Category": list(response.keys()),
                "Total": [response[category]["total"] for category in response],
                "Percentage":[response[category]["percentage"] for category in response]
            }
            df = pd.DataFrame(data)
            df_sorted = df.sort_values(by="Percentage",ascending=False)
            
            st.title("Expenses by category")
            st.bar_chart(data=df_sorted.set_index("Category")["Percentage"])
            
            df_sorted['Total'] = df_sorted['Total'].map("{:.2f}".format)
            df_sorted['Percentage'] = df_sorted['Percentage'].map("{:.2f}".format)
            
            st.table(df_sorted)
            # st.write(response)