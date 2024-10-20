import pandas as pd
import os
import repository.exec_insert_query as eq


def insert_cities():
  path = f'{os.path.abspath(".")}/data_base/xlsx/CVLI.xlsx'
  df_cvli = pd.read_excel(path)
  column_0 = df_cvli.columns[0]
  municipios = df_cvli[column_0].values[1: -1]

  insert = ""

  insert_municipio = f"""
    INSERT INTO 
    Municipio (nome, estado_id) 
    VALUES 
  """
  for municipio in municipios:
    insert += f"  ('{municipio}', 1),\n"

  insert_municipio += f"{insert[:-2]};"

  eq.exec_query(insert_municipio)
  # print(insert_municipio)