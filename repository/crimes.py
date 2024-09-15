from mysql_connection import get_connection as _get_connection
import repository.exec_query as eq


def get_crime_options():
  query = "SELECT * FROM Crime"
  result = eq.exec_query(query=query)
  
  return result