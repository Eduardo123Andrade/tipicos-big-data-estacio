from mysql_connection import get_connection as _get_connection

def _query_build(year=None):
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
    if year and year != 'Todos':
        query += f" AND cm.ano = '{year}'"

    query += ' GROUP BY m.nome'
    return query

def get_all_crimes():
  connection = _get_connection()
  cursor = connection.cursor()
  query = _query_build()
  cursor.execute(query)
  
  return _fetch_and_close_connection(cursor=cursor, connection=connection)

def get_crimes_by_year(year):
  connection = _get_connection()
  cursor = connection.cursor()
  query = _query_build(year=year)
  cursor.execute(query)

  return _fetch_and_close_connection(cursor=cursor, connection=connection)

def _fetch_and_close_connection(cursor, connection):
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result
