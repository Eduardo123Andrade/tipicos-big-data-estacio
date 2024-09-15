import streamlit as st
import pandas as pd
from charts.all_crimes import get_all_crimes
from dashboard_support.year_options import year_options
from dashboard_support.crime_options import get_crime_options
from dashboard_support.city_options import get_cities_options
from charts.crimes_city import crimes_city
from charts.crime_per_city import crimes_per_city


st.set_page_config(layout="wide")

initial_year = st.sidebar.selectbox("Inicio", year_options)
final_year = st.sidebar.selectbox("Fim", year_options)

def format_crime_option(crime):
  return crime["description"]

def format_city_options(city):
    return city["description"]

crime_option = st.sidebar.selectbox("Crimes", get_crime_options(), format_func=format_crime_option)
crime_id = crime_option["id"]

city_options = st.sidebar.selectbox("Cidades", get_cities_options(), format_func=format_city_options)
city_id = city_options["id"]

all_crimes_pie_chart = get_all_crimes(initial_year=initial_year, final_year=final_year)
crime_city_chart = crimes_city(crime_id=crime_id, initial_year=initial_year, final_year=final_year)
crime_per_city_chart = crimes_per_city(city_id=city_id, initial_year=initial_year, final_year=final_year)

[pie_chart1]= st.columns(1)
bar_chart1, bar_chart2 = st.columns(2)

pie_chart1.plotly_chart(all_crimes_pie_chart)
bar_chart1.plotly_chart(crime_city_chart)
bar_chart2.plotly_chart(crime_per_city_chart)
