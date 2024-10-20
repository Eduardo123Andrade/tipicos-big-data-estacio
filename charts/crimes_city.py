import repository.crime_on_city as coc
import pandas as pd
import plotly.express as px

def crimes_city(city_ids, initial_year=None, final_year=None):
  result = coc.get_crime_on_city(city_ids=city_ids, initial_year=initial_year, final_year=final_year)

  return _format_data_frame(result)

  
def _format_data_frame(query_result):
  df = pd.DataFrame(query_result, columns=['Cidade', 'Quantidade'])
  
  fig_date = px.bar(
    df, 
    x="Quantidade",
    y="Cidade",
    title="Crimes por Cidade",
    orientation="h",
  )

  return fig_date.update_traces(text=df["Quantidade"])
