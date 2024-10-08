
# import repository.insert_cities as ri
import repository.insert_city_crimes as rcc

def insert_all_data():
  # try:
    # ri.insert_cities()
  rcc.insert_city_crimes()
    # print()
  # except:
  #   print("data already exists")
  
  print("finish")
  