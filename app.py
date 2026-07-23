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

    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Sucesso</title>

<style>

body{
    margin:0;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
    background:#f4f4f4;
    font-family:Arial, sans-serif;
}

.card{
    background:white;
    padding:40px;
    border-radius:12px;
    box-shadow:0 0 20px rgba(0,0,0,.15);
    text-align:center;
}

h1{
    color:green;
}

</style>

</head>

<body>

<div class="card">
    <h1>IP registrado com sucesso!</h1>
</div>

</body>
</html>
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