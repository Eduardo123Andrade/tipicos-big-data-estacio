from repository.set_date_filter_on_query import set_date_on_query
import repository.exec_query as eq

def _query_build(city_ids, initial_year=None, final_year=None):
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
    query += f'AND cm.municipio_id IN {tuple(city_ids)}'
    query += set_date_on_query(initial_year=initial_year, final_year=final_year)

    query += ' GROUP BY m.nome;'

    return query

def get_all_crimes(city_ids):
  query = _query_build(city_ids=city_ids)
  result = eq.exec_query(query)
  
  return result

def get_crimes_by_year(city_ids, initial_year, final_year=None):
  query = _query_build(city_ids=city_ids, initial_year=initial_year, final_year=final_year)
  result = eq.exec_query(query)

  return result
