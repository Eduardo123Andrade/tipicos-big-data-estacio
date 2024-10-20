import pandas as pd
import os
import repository.exec_insert_query as eq


def insert_city_crimes_mdfcm():
  path = f'{os.path.abspath(".")}/data_base/xlsx/VDFCM.xlsx'
  df_vdfcm = pd.read_excel(path)
  column_0 = df_vdfcm.columns[0]
  
  year_columns = df_vdfcm.columns[1:]

  relation_data = ""
  
  cities = df_vdfcm[column_0].values[2: -1].tolist()

  for city in cities:
    index = cities.index(city)
    for column in year_columns:
      year = int(df_vdfcm[column].values[1])
      quantity = int(str(df_vdfcm[column].values[index + 3]).replace(".", ""))
      relation_data += f"""(
        {year}, 
        {quantity}, 
        (SELECT m.id FROM Municipio m WHERE m.nome = '{city}'), 
        (SELECT c.id FROM Crime c WHERE c.sigla = 'VDFCM')),
        """

  insert_crime_municipio = f"""
  INSERT INTO TOPICOS_BIGDATA.Crime_Municipio
  (ano, quantidade, municipio_id, crime_id)
  VALUES
  """
  insert_crime_municipio += f"{relation_data[:-10]};"
  
  eq.exec_query(insert_crime_municipio)