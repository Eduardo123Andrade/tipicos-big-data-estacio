from mysql_connection import get_connection as _get_connection

_query_by_year = '''
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

_full_query ='''
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


def get_all_crimes():
  connection = _get_connection()
  cursor = connection.cursor()
  cursor.execute(_full_query)
  
  return _fetch_and_close_connection(cursor=cursor, connection=connection)

def get_crimes_by_year(year):
  connection = _get_connection()
  cursor = connection.cursor()
  cursor.execute(_query_by_year, (year, ))

  return _fetch_and_close_connection(cursor=cursor, connection=connection)

def _fetch_and_close_connection(cursor, connection):
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result
