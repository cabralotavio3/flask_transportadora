from database import db

class Usuario(db.Model):
    __tablename__= "Transportadoras"
    id_transportadora = db.Column(db.Integer, primary_key=True)
    nome= db.Column(db.String(100))
    contato = db.Column(db.String(100))
    regiao_atuacao= db.Column(db.String(100))

    def __init__(self, nome, contato,regiao_atuacao):
        self.nome = nome
        self.contato = contato
        self.regiao_atuacao = regiao_atuacao

    def __repr__(self):
        return"<Nome{}>".format(self.nome)