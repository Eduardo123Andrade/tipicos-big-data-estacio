from mysql_connection import get_connection as _get_connection

query = '''
SELECT
	m.nome,
    	(
		SELECT sum(cm2.quantidade) FROM Crime_Municipio cm2 
		WHERE cm2.crime_id = c.id AND cm2.municipio_id = m.id
	) AS qtd_crime
FROM Crime_Municipio cm 
LEFT JOIN Municipio m ON cm.municipio_id  = m.id
LEFT JOIN Crime c ON cm.crime_id = c.id 
WHERE c.id = %s
GROUP BY m.nome , c.descricao, qtd_crime;
'''

def get_crime_on_city(crime_id):
    connection = _get_connection()
    cursor = connection.cursor()
    cursor.execute(query, (crime_id,))
    
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result