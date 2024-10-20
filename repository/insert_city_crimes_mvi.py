import pandas as pd
import os
import repository.exec_insert_query as eq


def insert_city_crimes_mvi():
  path = f'{os.path.abspath(".")}/data_base/xlsx/MVI.xlsx'
  df_mvi = pd.read_excel(path)
  column_0 = df_mvi.columns[0]
  
  year_columns = df_mvi.columns[1:]

  relation_data = ""
  
  cities = df_mvi[column_0].values[1: -1].tolist()

  for city in cities:
    index = cities.index(city)
    for column in year_columns:
      year = int(df_mvi[column].values[0])
      quantity = int(str(df_mvi[column].values[index + 1]).replace(".", ""))
      relation_data += f"""(
        {year}, 
        {quantity}, 
        (SELECT m.id FROM Municipio m WHERE m.nome = '{city}'), 
        (SELECT c.id FROM Crime c WHERE c.sigla = 'MVI')),
        """

  insert_crime_municipio = f"""
  INSERT INTO TOPICOS_BIGDATA.Crime_Municipio
  (ano, quantidade, municipio_id, crime_id)
  VALUES
  """
  insert_crime_municipio += f"{relation_data[:-10]};"
  
  eq.exec_query(insert_crime_municipio)