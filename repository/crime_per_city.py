from repository.set_date_filter_on_query import set_date_on_query
import repository.exec_query as eq

def _query_build(city_ids, initial_year, final_year=None):
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
    query += f" AND m.id IN {tuple(city_ids)}"

    query += set_date_on_query(initial_year=initial_year, final_year=final_year)

    query += '''
    GROUP BY
      m.nome,
      c.sigla,
      c.descricao;
    '''
    return query

def get_crime_per_city(city_ids, initial_year=None, final_year=None):
    query = _query_build(city_ids=city_ids, initial_year=initial_year, final_year=final_year)
    result = eq.exec_query(query=query)
    
    return result