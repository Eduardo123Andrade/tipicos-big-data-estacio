import mysql.connector as connection
import pandas as pd

# try:
#     mydb = connection.connect(host="localhost", database = 'TOPICOS_BIGDATA',user="root", passwd="mysqlPW",use_pure=True)
#     query = "Select * from Estado;"
#     result_dataFrame = pd.read_sql(query,mydb)
#     result = result_dataFrame.head()
#     mydb.close() #close the connection
# except Exception as e:
#     mydb.close()
#     print(str(e))


def get_connection():
  try:
      mydb = connection.connect(host="localhost", database = 'TOPICOS_BIGDATA',user="root", passwd="mysqlPW",use_pure=True)
      return mydb
  except Exception as e:
      mydb.close()
      print(str(e))