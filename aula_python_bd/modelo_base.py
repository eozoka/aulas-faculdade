import oracledb

conn = oracledb.connect(user='-------' , password='-------' , dsn='oracle.fiap.com.br/orcl')
print('Database version', conn.version)

cur = conn.cursor()
cur.execute('SELECT * FROM T_MENSAGEM') 

rows = cur.fetchall()
for reg in rows:
    print(reg)

cur.close()
conn.close()