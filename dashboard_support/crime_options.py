import repository.crimes as rc

def map_crime_result(crime):
    (id, description, abbreviation) = crime
    return {"id": id, "description": f"{description} - ({abbreviation})"}

def get_crime_options():
  result = rc.get_crime_options()

  options = list(map(map_crime_result, result))

  return options
