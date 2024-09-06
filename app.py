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
from models import Transportadora

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

@app.route('/Transportadora')
def Transportadoras():
    u = Transportadora.query.all()
    return render_template('transportadora_lista.html', dados_html = u)

@app.route('/Transportadora/add')
def usuario_add():
    u = Transportadora.query.all()
    return render_template('transportadora_add.html', dados_html = u)

@app.route('/Transportadora/save', methods=['POST'])
def usuario_save():
    nome = request.form.get('nome')
    contato = request.form.get('contato')
    regiao_atuacao = request.form.get('regiao_atuacao')
    if nome and contato and regiao_atuacao:
        usuario_transportadora = Transportadora(nome, contato, regiao_atuacao)
        db.session.add(usuario_transportadora)
        db.session.commit()
        flash('usuario cadastrado com sucesso!!')
        return redirect('/Transportadora')
    else:
        flash('preencha todos os campos!')
        return redirect('/Transportadora/add')

@app.route('/Transportadora/remove/<int:id_transportadora>')
def usuario_remove(id_transportadora):
    if id > 0:
        usuario_transportadora = Transportadora.query.get(id_transportadora)
        db.session.delete(usuario_transportadora)
        db.session.commit()
        flash('Removido Com sucesso!!')
        return redirect('/Transportadora')
    else:
        flash('Houve um erro.')
        return redirect('/Transportadora')
    
@app.route('/Transportadora/edita/<int:id>')
def usuario_edita(id_transportadora):
        usuario_transportadora = Transportadora.query.get(id_transportadora)
        return render_template('transportadora_edita.html', dados_html=usuario_transportadora)

@app.route('/Transportadora/editasave', methods = ['POST'])
def transportadora_editasave():
    id_transportadora = request.form.get('id_transportadora')
    nome = request.form.get('nome')
    contato = request.form.get('contato')
    regiao_atuacao = request.form.get('regiao_atuacao')
    if id_transportadora and nome and contato and regiao_atuacao:
        usuario_transportadora = Transportadora.query.get(id_transportadora)
        usuario_transportadora.nome = nome
        usuario_transportadora.contato = contato
        usuario_transportadora.regiao_atuacao = regiao_atuacao
        db.session.commit()
        flash('Dados atualizados com sucesso!!')
        return redirect('/Transportadora')
    else:
        flash('Está faltando dados!')
        return redirect('/Transportadora')
@app.route
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()