from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)

ARQUIVO = "ips.txt"


@app.route("/")
def home():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ip = ip.split(",")[0].strip()

    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{horario} | {ip}\n")

    return f"""
    <h1>IP registrado com sucesso!</h1>

    <h2>Seu IP:</h2>

    <h3>{ip}</h3>

    <br>

    <a href="/ips">Ver todos os IPs registrados</a>
    """


@app.route("/ips")
def listar():

    if not os.path.exists(ARQUIVO):
        return "Nenhum IP registrado."

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        dados = f.read()

    return f"<pre>{dados}</pre>"


if __name__ == "__main__":
    app.run(debug=True)