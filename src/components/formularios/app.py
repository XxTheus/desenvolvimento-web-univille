from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    # dados = request.args
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    dataNascimento = request.form.get('dataNascimento')
    chocolate = request.form.get('chocolate')
    coquinha = request.form.get('coquinha')
    sexo = request.form.get('sexo')
    cores = request.form.get('cores')
    texto = request.form.get('texto')
    return f"<h1>{usuario}</h1><h1>{senha}</h1><h1>{dataNascimento}</h1><h3>Chocolate: {chocolate} Coquinha: {coquinha}</h3><h3>{sexo}</h3><h3>Cor: {cores}</h3><h3> Você digitou: {texto}</h3"

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
                <input type="email" id="txtUsuario" name="usuario" placeholder="Digite seu Usuário">
            </fieldset>
            <fieldset>
                <label for="txtData">Sua data de Nascimento</label>
                <input type="date" name="dataNascimento">
            </fieldset>
            <fieldset>
                <label for="txtCheck">Qual você gosta?</label>
                <input type="checkBox" name="chocolate">Chocolate
                <input type="checkBox" name="coquinha">Coca-cola
            </fieldset>
            <fieldset>
                <label for="txtSexo">Qual é o seu sexo</label>
                <input type="radio" name="sexo" value="Masculino">Masculino
                <input type="radio" name="sexo" value="Feminino">Feminino
            </fieldset>
            <fieldset>
                <label for="txtsenha">Senha</label>
                <input type="password" id="txtsenha" name="senha" placeholder="Digite sua senha" required>
            </fieldset>
            <fieldset>
                <label for="txtsenha">Seu arquivo</label>
                <input type="file" name="file">
            </fieldset>
            <fieldset>
                <input type="text" name="textFixo" value="Não da para alterar :)" readonly="readonly" disabled> 
            </fieldset>
            <fieldset>
                <select name="cores" placeholder="">
                    <option value="0"></option>
                    <option value="1">Azul</option>
                    <option value="2">Verde</option>
                    <option value="3">Vermelho</option>
                </select>
            </fieldset>
            <fieldset>
                <textarea rows="10" cols="30" name="texto">
                </textarea>
            </fieldset>
            <input type="submit">
            <!--<button type="submit">Enviar</button>-->
        </form>
    </body>
</html>
    '''