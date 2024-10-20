import repository.exec_query as eq

def get_all_cites():
  query = "SELECT m.id, m.nome FROM Municipio m;"
  return eq.exec_query(query)