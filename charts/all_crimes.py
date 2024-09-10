from mysql_connection import get_connection
import pandas as pd
import plotly.express as px

query_by_year = '''
SELECT 
  m.nome AS municipio,
  COALESCE(SUM(cm.quantidade), 0) AS 'quantidade crime'
FROM
  Municipio m
LEFT JOIN Crime_Municipio cm ON cm.municipio_id = m.id
WHERE
  cm.ano = %s  -- Use positional parameter for security
GROUP BY m.nome
'''

full_query ='''
SELECT 
	m.nome as municipio,
	(
	SELECT
		SUM(cm.quantidade)
	FROM
		Crime_Municipio cm
	WHERE
		cm.municipio_id = m.id
) as 'quantidade crime'
FROM
	Municipio m;
'''

def format_data_frame(query_result):
  df = pd.DataFrame(query_result, columns=['Municipio', 'Quantidade'])
  fig_date = px.pie(
    df, 
    values='Quantidade', 
    names='Municipio', 
    title='Crimes por municipio',
    labels='Quantidade',
  )
  return fig_date.update_traces(text=df['Quantidade'], textposition='inside', textinfo='text+percent')


def get_all_crimes(year):
  connection = get_connection()
  cursor = connection.cursor()
  if year ==  'Todos':
    cursor.execute(full_query)
  else:
    cursor.execute(query_by_year, (year, ))

  result = cursor.fetchall()
  cursor.close()
  return format_data_frame(result)

  
