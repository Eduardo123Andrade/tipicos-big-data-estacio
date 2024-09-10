from mysql_connection import get_connection as _get_connection

def _query_build(crime_id, year=None):
    query = '''
    SELECT
      m.nome,
      COALESCE(SUM(cm.quantidade), 0) AS qtd_crime
    FROM Crime_Municipio cm
    LEFT JOIN Municipio m ON cm.municipio_id = m.id
    LEFT JOIN Crime c ON cm.crime_id = c.id
    WHERE
	    1 = 1
    '''
    query += f" AND c.id = '{crime_id}'"

    if year and year != 'Todos':
        query += f" AND cm.ano = '{year}'"

    query += " GROUP BY m.nome;"

    return query

def get_crime_on_city(crime_id, year=None):
    connection = _get_connection()
    cursor = connection.cursor()
    query = _query_build(crime_id=crime_id, year=year)
    cursor.execute(query)
    
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result