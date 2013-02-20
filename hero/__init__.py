from flask import Flask, render_template
from loremipsum import Generator
from random import choice
import random
import string

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/passwd/')
@app.route('/passwd/<int:tamanho>/')
def passwd(tamanho=8):
	caracteres = string.punctuation + \
	             string.letters + \
	             string.digits
	senhas = [''.join([choice(caracteres) for x in range(tamanho)]) for x in range(10)]
	return render_template('senha.html', senhas=senhas)


@app.route('/lipsum/')
@app.route('/lipsum/<qtd>/')
def lipsum(qtd=1):
	g = Generator()
	#qtd = 6
	lip = '<br><br>'.join([x[2] for x in g.generate_paragraphs(int(qtd),True)])
	return render_template('lipsum.html', lip=lip)
