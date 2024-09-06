#pip install flask
#pip install Flask-SQLAlchemy
#pip install Flask-Migrate
#pip install Flask-Script
#pip install pymysql
#flask db init
#flask db migrate -m "Migracao inicial"
#flask db upgrade
from flask import Flask, render_template, request, flash, redirect
from database import db
from flask_migrate import Migrate
from models import Usuario

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

#drive://usuario:senha@servidor/banco_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/transporte"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuario')
def Transportadoras():
    u = Usuario.query.all()
    return render_template('usuario_lista.html', dados_html = u)

@app.route('/usuario/add')
def usuario_add():
    u = Usuario.query.all()
    return render_template('usuario_add.html', dados_html = u)

@app.route('/usuario/save', methods=['POST'])
def usuario_save():
    nome = request.form.get('nome')
    contato = request.form.get('contato')
    regiao_atuacao = request.form.get('regiao_atuacao')
    if nome and contato and regiao_atuacao:
        usuario = Usuario(nome, contato, regiao_atuacao)
        db.session.add(usuario)
        db.session.commit()
        flash('usuario cadastrado com sucesso!!')
        return redirect('/usuario')
    else:
        flash('preencha todos os campos!')
        return redirect('/usuario/add')

@app.route('/usuario/remove/<int:id_transportadora>')
def usuario_remove(id_transportadora):
    if id > 0:
        usuario = Usuario.query.get(id_transportadora)
        db.session.delete(usuario)
        db.session.commit()
        flash('Removido Com sucesso!!')
        return redirect('/usuario')
    else:
        flash('Houve um erro.')
        return redirect('/usuario')
    
@app.route('/usuario/edita/<int:id>')
def usuario_edita(id_transportadora):
        usuario = Usuario.query.get(id_transportadora)
        return render_template('usuario_edita.html', dados_html=usuario)

@app.route('/usuario/editasave', methods = ['POST'])
def usuario_editasave():
    id_transportadora = request.form.get('id_transportadora')
    nome = request.form.get('nome')
    email = request.form.get('email')
    idade = request.form.get('idade')
    if id_transportadora and nome and email and idade:
        usuario = Usuario.query.get(id_transportadora)
        usuario.nome = nome
        usuario.email = email
        usuario.idade = idade
        db.session.commit()
        flash('Dados atualizados com sucesso!!')
        return redirect('/usuario')
    else:
        flash('Está faltando dados!')
        return redirect('/usuario')
@app.route
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()