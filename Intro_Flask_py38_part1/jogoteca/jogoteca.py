from flask import Flask, render_template, request, redirect, session, flash
from Jogo import Jogo

# __name__= Indica que a aplicacao ira executar neste mesmo codigo
app = Flask(__name__)
# 'secret_key'= necessario para utilizar os cookies (session) o que indica uma "assinatura" de criptografia
app.secret_key = "alura"

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Ação', 'SNES')
lista = [jogo1, jogo2, jogo3]

@app.route("/")
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route("/novo")
def novo():
    return render_template('novo.html', titulo='Novo jogo')

@app.route("/criar", methods=['POST',])
def criar():
# request = Helper do Flask para obter o valor do campo dentro do form (HTML), de acordo com o "name" da tag
    nome = request.form['nome']
    # O 'form'= retorna um dicionario e o acesso eh feito pela key
    # ['categoria'] refere-se pelo campo ('name="categoria"') do HTML
    categoria = request.form['categoria']
    console = request.form['console']
    jogo_novo = Jogo(nome, categoria, console)
    lista.append(jogo_novo)
    return redirect('/')

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/autenticar", methods=['POST', ])
def autenticar():
    if 'mestra' == request.form['senha']:
# 'sesion'= armazena informacoes por mais de 1 ciclo de request (cria coockie no client)
        session['usuario_logado'] = request.form['usuario']
        flash(f'Usuário \"{session["usuario_logado"]}\" está logado!!!')
        return redirect('/')
    else:
        flash(f'Usuário \"{session["usuario_logado"]}\" NÃO está logado!!!')
        return redirect('/login')

app.run(debug=True)
