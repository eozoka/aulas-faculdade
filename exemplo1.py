import oracledb

#criar conexao com o banco
conn = oracledb.connect(user="rm567593" , password="230505" , dsn="oracle.fiap.com.br/orcl")

print(conn.version)
#abrindo cursor: servepara comunicar com o banco
cur = conn.cursor()
cur.execute('SELECT * FROM T_PS_MENSAGEM') 
rows = cur.fetchall()

for reg in rows:
    print(reg)

cur.close()
conn.close()