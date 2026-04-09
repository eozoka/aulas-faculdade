from faker import Faker
import random

fake = Faker("pt_BR")

convs = [
    "Amil", "Bradesco Saúde", "SulAmérica", "Unimed",
    "Porto Seguro Saúde", "SUS", "Hapvida",
    "NotreDame Intermédica", "Care Plus", "Golden Cross"
]

sql = []

for _ in range(100):
    nome = fake.name()
    nascimento = fake.date_of_birth().strftime("%d/%m/%Y")
    telefone = fake.phone_number()
    convenio = random.choice(convs)

    comando = f"""
    INSERT INTO T_PS__PACIENTE(nome, nascimento, telefone, convenio)
    VALUES ('{nome}', TO_DATE('{nascimento}', 'DD/MM/YYYY'), '{telefone}', '{convenio}');
    """

    sql.append(comando)

for s in sql[:5]:
    print(s)