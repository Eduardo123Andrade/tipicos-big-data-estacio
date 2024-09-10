import streamlit as st
import pandas as pd
import plotly.express as px
from charts.all_crimes import get_all_crimes
from dashboard_support.year_options import year_options
from dashboard_support.crime_options import get_crime_options

st.set_page_config(layout="wide")

year = st.sidebar.selectbox("Ano", year_options)

def format_crime_option(crime):
  return crime["description"]

crime_option = st.sidebar.selectbox("Crimes", get_crime_options(), format_func=format_crime_option)
crime_id = crime_option["id"]

print(crime_id)

col1, col2 = st.columns(2)

all_crimes_pie_chart = get_all_crimes(year)

col1.plotly_chart(all_crimes_pie_chart)

 