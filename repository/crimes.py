from mysql_connection import get_connection as _get_connection

query = "SELECT * FROM Crime"

def get_crime_options():
  connection = _get_connection()
  cursor = connection.cursor()
  cursor.execute(query)

  result = cursor.fetchall()

  cursor.close()
  connection.close()
  return result