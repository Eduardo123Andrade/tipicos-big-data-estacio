import pandas as pd
import os
import repository.exec_insert_query as eq


def insert_city_crimes_ccp():
  path = f'{os.path.abspath(".")}/data_base/xlsx/CCP.xlsx'
  df_ccp = pd.read_excel(path)
  column_0 = df_ccp.columns[0]

  year_columns = df_ccp.columns[1:] 

  cities = df_ccp[column_0].values[3: -1].tolist()
  
  relation_data = ""
  
  for city in cities:
    index = cities.index(city)
    for column in year_columns:
      year = int(df_ccp[column].values[2])
      quantity = int(str(df_ccp[column].values[index + 3]).replace(".", ""))
      relation_data += f"""(
        {year}, 
        {quantity}, 
        (SELECT m.id FROM Municipio m WHERE m.nome = '{city}'), 
        (SELECT c.id FROM Crime c WHERE c.sigla = 'CCP')),
        """
  insert_crime_municipio = f"""
  INSERT INTO TOPICOS_BIGDATA.Crime_Municipio
  (ano, quantidade, municipio_id, crime_id)
  VALUES
  """
  insert_crime_municipio += f"{relation_data[:-10]};"
  
  eq.exec_query(insert_crime_municipio)