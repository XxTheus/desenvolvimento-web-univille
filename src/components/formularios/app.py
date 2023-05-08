from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    dados = request.args
    if dados['nome'] == "Matheus":
        return f"<p>{dados['nome']} Válido</p>"
    else:
        return f"<p>{dados['nome']} Inválido</p>"
    #return f"<p>Nome {dados['nome']}</p>"