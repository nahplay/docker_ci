# pylint: disable=C0114
import psycopg2

secrets = []
with open("env_variables", encoding='utf-8') as f:
    for i in f:
        secrets.append(i.replace('\n','').split('=')[1])

conn = psycopg2.connect(
    host="postgres",#good with containter name or "host.docker.internal" locally,
                    # reconsider in case of clustring/cloud
    database=secrets[0],
    user=secrets[1],
    password=secrets[2])

cur = conn.cursor()

cur.execute('create table test (value integer)')
conn.commit()
conn.close()
