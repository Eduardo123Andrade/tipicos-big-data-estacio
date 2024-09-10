import pandas as pd
import plotly.express as px
import repository.city_crimes as rcc


def get_all_crimes(year):
  if year ==  'Todos':
    result = rcc.get_all_crimes()
    # print(result)
    return _format_data_frame(result)
  
  result = rcc.get_crimes_by_year(year=year)
  return _format_data_frame(result)
  
def _format_data_frame(query_result):
  df = pd.DataFrame(query_result, columns=['Municipio', 'Quantidade'])
  fig_date = px.pie(
    df, 
    values='Quantidade', 
    names='Municipio', 
    title='Crimes por municipio',
    labels='Quantidade',
  )
  return fig_date.update_traces(
    text=df['Quantidade'], 
    textposition='inside', 
    textinfo='text+percent'
    )
