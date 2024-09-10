from mysql_connection import get_connection


query = "SELECT * FROM Crime"

def map_crime_result(crime):
    (id, description, abbreviation) = crime
    return {"id": id, "description": f"{description} - ({abbreviation})"}

def get_crime_options():
  connection = get_connection()
  cursor = connection.cursor()
  cursor.execute(query)

  result = cursor.fetchall()

  options = list(map(map_crime_result, result))

  cursor.close()
  return options
