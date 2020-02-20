import psycopg2
from contextlib import closing


conn = psycopg2.connect(dbname='avitodb', user='vlad', password='', host='localhost')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS a_data (
                
               );''')



