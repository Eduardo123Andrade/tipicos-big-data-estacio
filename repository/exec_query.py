from mysql_connection import get_connection as _get_connection

def exec_query(query =""):
    connection = _get_connection()
    cursor = connection.cursor()
    cursor.execute(query)

    result = cursor.fetchall()
    
    cursor.close()
    connection.close()

    return result