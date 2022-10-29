# pylint: disable=C0114
import psycopg2
import os


secrets = []
database = os.environ['database']
user = os.environ['user']
password = os.environ['password']

conn = psycopg2.connect(
    host="postgres",
    database=database,
    user=user,
    password=password)

try:
    cur = conn.cursor()
    cur.execute('create table test (value integer)')
    conn.commit()
    conn.close()
    print('SUCCESS')
except:
    print("YOU'VE DUN GOOFED")
    raise
