from flask import Flask, render_template, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'chave_secreta_meus_filmes'

FILMES = {
    1: {'id': 1, 'titulo': 'Frozen', 'ano': 2005, 'duracao': 178},
    2: {'id': 2, 'titulo': 'Sendokai Champions Sengate',       'ano': 2021, 'duracao': 169},
    3: {'id': 3, 'titulo': 'Vingadores: Guerra Infinita',           'ano': 2019, 'duracao': 132},
    4: {'id': 4, 'titulo': 'Miraculous Ladybug Londres',     'ano': 2022, 'duracao': 130},
}

@app.route('/')
def filmes():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)