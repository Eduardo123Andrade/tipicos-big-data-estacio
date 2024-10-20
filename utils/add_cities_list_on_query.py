

def add_cities_id_list_on_query(city_ids):
  if(len(city_ids) == 1):
    return f"AND cm.municipio_id = '{city_ids[0]}'"
  else:
    return f" AND cm.municipio_id IN {tuple(city_ids)}"
