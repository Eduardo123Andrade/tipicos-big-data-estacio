import pandas as pd
import plotly.express as px
import repository.cities as rc

def _map_city_result(city):
    (id, nome) = city
    return {"id": id, "description": nome}


def get_cities_options():
  result = rc.get_all_cites()

  options = list(map(_map_city_result, result))

  return options


  
