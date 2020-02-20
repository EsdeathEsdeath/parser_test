import psycopg2
from contextlib import closing
import csv


def treatment_csv(data):


conn = psycopg2.connect(dbname='avitodb', user='vlad', password='', host='localhost')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS a_data (
                
               );''')



