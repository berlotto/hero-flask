from flask import Flask, render_template
from loremipsum import Generator
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/lipsum/')
def lipsum():
	g = Generator()
	qtd = 6
	return '<br><br>'.join([x[2] for x in g.generate_paragraphs(qtd,True)])
