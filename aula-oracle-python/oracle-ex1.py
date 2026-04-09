
import oracledb

def get_conexao():
    return oracledb.connect(user="--------",password="-------",dsn="oracle.fiap.com.br/ORCL")

if __name__ == "__main__":
    nome = input("Digite o nome do paciente: ")
    nascimento = input("Digite a data de nascimento (dd/mm/yyyy): ")
    telefone = input("Digite o telefone: ")
    convenio = input("Digite o convênio: ")

    paciente = {'nome': nome,'nascimento': nascimento,'telefone': telefone,'convenio': convenio}

    sql = """
        INSERT INTO T_PS__PACIENTE (nome, nascimento, telefone, convenio)
        VALUES (:nome, TO_DATE(:nascimento, 'DD/MM/YYYY'), :telefone, :convenio)
    """

    with get_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, paciente)
            conexao.commit()

    print("Paciente inserido com sucesso!")