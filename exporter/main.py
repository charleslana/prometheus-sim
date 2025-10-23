from flask import Flask, Response
import random
import string
import uuid

app = Flask(__name__)

# Listas globais para armazenar usuários e endereços
usuarios = []
enderecos = []

def gerar_nome():
    primeiros = ["Ana", "Carlos", "João", "Maria", "Lucas", "Fernanda", "Paula", "Bruno"]
    sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Costa", "Pereira", "Lima", "Gomes"]
    return f"{random.choice(primeiros)} {random.choice(sobrenomes)}"

def gerar_email(nome):
    dominio = random.choice(["gmail.com", "hotmail.com", "outlook.com", "empresa.com"])
    nome_email = nome.lower().replace(" ", ".")
    return f"{nome_email}@{dominio}"

def gerar_cpf():
    return "".join(random.choices(string.digits, k=11))

def gerar_endereco():
    ruas = ["Av. Paulista", "Rua das Flores", "Rua Central", "Rua do Sol", "Av. Atlântica"]
    cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Porto Alegre", "Belo Horizonte"]
    estados = ["SP", "RJ", "PR", "RS", "MG"]
    paises = ["BR", "US", "AR", "CL", "PT"]
    return {
        "rua": random.choice(ruas),
        "numero": str(random.randint(1, 9999)),
        "cidade": random.choice(cidades),
        "estado": random.choice(estados),
        "pais": random.choice(paises),
    }

@app.route("/metrics")
def metrics():
    # Gerar novo usuário
    id_usuario = str(uuid.uuid4())
    nome = gerar_nome()
    email = gerar_email(nome)
    cpf = gerar_cpf()
    endereco = gerar_endereco()

    # Adicionar às listas globais
    usuarios.append({
        "id": id_usuario,
        "nome": nome,
        "email": email,
        "cpf": cpf
    })
    enderecos.append({
        "id": id_usuario,
        **endereco
    })

    # Construir métricas para todos os usuários gerados
    lines = []
    for u in usuarios:
        lines.append(
            f'usuarios_info{{id="{u["id"]}", nome="{u["nome"]}", email="{u["email"]}", cpf="{u["cpf"]}"}} 1'
        )
    for e in enderecos:
        lines.append(
            f'usuarios_endereco{{id="{e["id"]}", rua="{e["rua"]}", numero="{e["numero"]}", cidade="{e["cidade"]}", estado="{e["estado"]}", pais="{e["pais"]}"}} 1'
        )

    data = "\n".join(lines) + "\n"
    return Response(data, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
