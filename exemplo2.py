import oracledb

conn = oracledb.connect(user='------' , password='--------' , dsn="oracle.fiap.com.br/orcl")

rem = input("Remetente: ")
dest = input("Destinatario: ")
assunto = input("Assunto: ")
conteudo = input("Conteudo: ")

dado = {"from": rem, "to": dest, "subject": assunto, "content": conteudo}

sql = "INSERT INTO T_PS_MENSAGEM(assunto, destinatario, conteudo, remetente) VALUES (:subject, :to, :content, :from)"

cur = conn.cursor()
cur.execute(sql, dado)

conn.commit()

cur.close()
conn.close()