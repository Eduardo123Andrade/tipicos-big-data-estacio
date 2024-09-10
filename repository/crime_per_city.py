from mysql_connection import get_connection as _get_connection
from repository.set_date_filter_on_query import set_date_on_query

def _query_build(city_id, initial_year, final_year=None):
    query = '''
    SELECT
      m.nome,
      c.descricao,
      c.sigla,
      COALESCE(SUM(cm.quantidade), 0) AS qtd_crime
    FROM Crime_Municipio cm
    LEFT JOIN Municipio m ON cm.municipio_id = m.id
    LEFT JOIN Crime c ON cm.crime_id = c.id
    WHERE
	    1 = 1
    '''
    query += f" AND m.id = '{city_id}'"

    query += set_date_on_query(initial_year=initial_year, final_year=final_year)

    query += '''
    GROUP BY
      m.nome,
      c.sigla,
      c.descricao;
    '''
    return query

def get_crime_per_city(city_id, initial_year=None, final_year=None):
    connection = _get_connection()
    cursor = connection.cursor()
    query = _query_build(city_id=city_id, initial_year=initial_year, final_year=final_year)
    cursor.execute(query)
    
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result