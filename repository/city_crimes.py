from mysql_connection import get_connection as _get_connection
from repository.set_date_filter_on_query import set_date_on_query

def _query_build(initial_year=None, final_year=None):
    query = '''
    SELECT 
      m.nome AS municipio,
      COALESCE(SUM(cm.quantidade), 0) AS 'quantidade crime'
    FROM
      Municipio m
    LEFT JOIN Crime_Municipio cm ON cm.municipio_id = m.id
    WHERE
      1 = 1
    '''
    query += set_date_on_query(initial_year=initial_year, final_year=final_year)

    query += ' GROUP BY m.nome'

    return query

def get_all_crimes():
  connection = _get_connection()
  cursor = connection.cursor()
  query = _query_build()
  cursor.execute(query)
  
  return _fetch_and_close_connection(cursor=cursor, connection=connection)

def get_crimes_by_year(initial_year, final_year=None):
  connection = _get_connection()
  cursor = connection.cursor()
  query = _query_build(initial_year=initial_year, final_year=final_year)
  cursor.execute(query)

  return _fetch_and_close_connection(cursor=cursor, connection=connection)

def _fetch_and_close_connection(cursor, connection):
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result