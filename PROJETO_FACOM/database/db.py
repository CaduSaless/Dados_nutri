from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app

db = SQLAlchemy()


class Cliente(db.Model):
	__tablename__ = 'tabela_clientes'
	id = db.Column(db.Integer, primary_key=True)
	CPF = db.Column(db.String(11), nullable=False)
	altura = db.Column(db.Float, nullable=False)
	peso = db.Column(db.Float, nullable=False)
	marcador01 = db.Column(db.String(20))
	marcador02 = db.Column(db.String(20))
	marcador03 = db.Column(db.String(20))
	marcador04 = db.Column(db.String(20))
	marcador05 = db.Column(db.String(20))
	marcador06 = db.Column(db.String(20))
	marcador07 = db.Column(db.String(20))
	marcador08 = db.Column(db.String(20))
	marcador09 = db.Column(db.String(20))
	marcador10 = db.Column(db.String(20))

def inserir_cliente(cpf, altura, peso,marcador01=None, marcador02=None, marcador03=None, marcador04=None, marcador05=None,marcador06=None, marcador07=None, marcador08=None, marcador09=None, marcador10=None):
	novo = Cliente(
		CPF=str(cpf),
		altura=altura,
		peso=peso,
		marcador01=marcador01,
		marcador02=marcador02,
		marcador03=marcador03,
		marcador04=marcador04,
		marcador05=marcador05,
		marcador06=marcador06,
		marcador07=marcador07,
		marcador08=marcador08,
		marcador09=marcador09,
		marcador10=marcador10
	)
	db.session.add(novo)
	db.session.commit()