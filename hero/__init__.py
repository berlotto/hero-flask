from flask import Flask
from loremipsum import Generator
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/lipsum/')
def lipsum():
	g = Generator()
	qtd = 6
	return '<br><br>'.join([x[2] for x in g.generate_paragraphs(qtd,True)])
