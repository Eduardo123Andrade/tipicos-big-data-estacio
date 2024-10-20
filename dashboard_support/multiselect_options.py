from dashboard_support.city_options import get_cities_options

def format_crime_option(crime):
  return crime["description"]


_default_cities_name = [
  "IGARASSU",
  "JABOATAO DOS GUARARAPES",
  "OLINDA",
  "PAULISTA",
  "RECIFE"
]


def multiselect_city_options(st):
  cities = get_cities_options()

  default_cities = list(filter(lambda city: city["description"] in _default_cities_name, cities))
  
  options = st.sidebar.multiselect(
      "What are your favorite colors",
      get_cities_options(),
      format_func=format_crime_option,
      max_selections=5,
      default=default_cities
  )

  city_ids = list(map(lambda city: city["id"], options))

  return city_ids
