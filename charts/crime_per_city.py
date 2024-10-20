import repository.crime_per_city as cpc
import pandas as pd
import plotly.express as px


def crimes_per_city(city_ids, crime_id, initial_year=None, final_year=None):
  result = cpc.get_crime_per_city(city_ids=city_ids, crime_id=crime_id, initial_year=initial_year, final_year=final_year)

  return _format_data_frame(result)


def _format_data_frame(query_result):
  df = pd.DataFrame(query_result, columns=[
    'Cidade',
    'Descrição',
    'Sigla', 
    'Ano',
    'Quantidade',
  ])
  
  fig_date = px.line(
    df, 
    x="Ano",
    y="Quantidade",
    
    color="Cidade",
    title="Evolução de Crimes por Cidade",
    labels="Descrição",
    hover_data="Descrição"
  )


  return fig_date.update_traces(text=df["Quantidade"])