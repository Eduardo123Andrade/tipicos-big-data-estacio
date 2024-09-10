import repository.crime_on_city as coc
import pandas as pd
import plotly.express as px

def crimes_city(crime_id, year=None):
  result = coc.get_crime_on_city(crime_id=crime_id, year=year)

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
