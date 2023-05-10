from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    # dados = request.args
    usuario = request.form.get('usuario')
    return f"<h1>{usuario}</h1>"

"""     if dados['nome'] == "Matheus":
        return f"<p>{dados['nome']} Válido</p>"
    else:
        return f"<p>{dados['nome']} Inválido</p>" 
"""

@app.route("/formulario")
def formulario():
    return '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <form action="http://localhost:5000/" method="POST">
            <fieldset>
                <label for="txtUsuario">Usuário</label>
                <input type="text"
                    id="txtUsuario"
                    name="usuario"
                    placeholder="Digite seu Usuário">
            </fieldset>
            <fieldset>
                <label for="txtSenha">Senha</label>
                <input type="password" 
                    name="Senha"
                    id="txtSenha"
                    placeholder="Digite sua Senha">
            </fieldset>
            <input type="submit">
            <!--
                <button type="submit">Enviar</button>
            -->
        </form>
    </body>
</html>
    '''