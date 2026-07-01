from flask import Flask, render_template, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'chave_secreta_meus_filmes'

FILMES = {
    1: {'id': 1, 'titulo': 'Frozen', 'ano': 2005, 'duracao': 178},
    2: {'id': 2, 'titulo': 'Sendokai Champions Sengate',       'ano': 2021, 'duracao': 169},
    3: {'id': 3, 'titulo': 'Vingadores: Guerra Infinita',           'ano': 2019, 'duracao': 132},
    4: {'id': 4, 'titulo': 'Miraculous Ladybug Londres',     'ano': 2022, 'duracao': 130},
}
app.config['FILMES'] = FILMES

@app.route('/')
def filmes():
    return render_template('index.html', filmes=app.config['FILMES'])

# Rota para watchlist
@app.route('/watchlist')
def watchlist():
    watchlist_ids = session.get('watchlist', [])
    filmes_watchlist = []
    duracao_total = 0
    
    # Monta a lista de filmes baseada nos IDs salvos na sessão
    for filme_id in watchlist_ids:
        if filme_id in app.config['FILMES']:
            filme = app.config['FILMES'][filme_id]
            filmes_watchlist.append(filme)
            duracao_total += filme['duracao']
            
    return render_template('index.html', filmes=filmes_watchlist, duracao_total=duracao_total)

if __name__ == '__main__':
    app.run(debug=True)