
import repository.insert_cities as ri

ri.insert_cities()

def insert_all_data():
  try:
    ri.insert_cities()
    # print()
  except:
    print("data already exists")
  
  print("finish")
  