import repository.crime_per_city as cpc
import pandas as pd
import plotly.express as px


def crimes_per_city(city_id, initial_year=None, final_year=None):
  result = cpc.get_crime_per_city(city_id=city_id, initial_year=initial_year, final_year=final_year)

  return _format_data_frame(result)


def _format_data_frame(query_result):
  df = pd.DataFrame(query_result, columns=[
    'Cidade',
    'Descrição',
    'Sigla', 
    'Quantidade'
  ])
  
  fig_date = px.bar(
    df, 
    x="Sigla",
    y="Quantidade",
    title="Crimes na Cidade",
    labels="Descrição",
    hover_data="Descrição"
    # orientation="h",
  )

  return fig_date.update_traces(text=df["Quantidade"])
