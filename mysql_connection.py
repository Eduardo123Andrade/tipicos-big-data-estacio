import mysql.connector as connection
import pandas as pd

def get_connection():
  try:
      mydb = connection.connect(host="localhost", database = 'TOPICOS_BIGDATA',user="root", passwd="mysqlPW",use_pure=True)
      return mydb
  except Exception as e:
      mydb.close()
      print(str(e))