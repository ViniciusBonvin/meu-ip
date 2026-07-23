from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    return f"""
    <h1>Seu IP é:</h1>
    <h2>{ip}</h2>
    """

if __name__ == "__main__":
    app.run(debug=True)