from flask import Flask, Response
import random

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    # Simulando 3 usuários
    usuarios = [
        {"id": "1", "pais": "BR", "plano": "premium"},
        {"id": "2", "pais": "US", "plano": "free"},
        {"id": "3", "pais": "BR", "plano": "free"},
    ]

    lines = []

    for u in usuarios:
        # usuarios_info
        lines.append(f'usuarios_info{{id="{u["id"]}", pais="{u["pais"]}", plano="{u["plano"]}"}} 1')

        # usuarios_atividade sempre existe
        atividade = random.randint(0, 10)
        lines.append(f'usuarios_atividade{{id="{u["id"]}"}} {atividade}')


    data = "\n".join(lines) + "\n"
    return Response(data, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
