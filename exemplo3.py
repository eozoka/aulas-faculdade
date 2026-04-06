import oracledb

conn = oracledb.connect(
    user="--------",
    password="---------",
    dsn="oracle.fiap.com.br/orcl"
)

cursor = conn.cursor()

print("Alterando remetente da msg: ")
id_mensagem = input("ID: ")
novo_rem = input("Remetente: ")

sql = """
UPDATE T_PS_MENSAGEM
SET REMETENTE = :remetente
WHERE ID_MENSAGEM = :id
"""

cursor.execute(sql, {
    "remetente": novo_rem,
    "id": id_mensagem
})

conn.commit()

print("Remetente atualizado com sucesso!")

cursor.close()
conn.close()