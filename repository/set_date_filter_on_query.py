def set_date_on_query(initial_year=None, final_year=None):
    query = ""

    if initial_year and final_year and initial_year != 'Todos' and final_year != 'Todos' and int(final_year) < int(initial_year):
      return query

    if initial_year and initial_year != 'Todos':
      query += f" AND cm.ano >= '{initial_year}'"

    if final_year and final_year != 'Todos':
      query += f" AND cm.ano <= '{final_year}'"

    return query
   