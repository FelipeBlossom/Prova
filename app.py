from flask import Flask, render_template, redirect, url_for, session, flash, request

app = Flask(__name__)
app.secret_key = 'chave_secreta_meus_filmes'

FILMES = {
    1: {'id': 1, 'titulo': 'Frozen', 'ano': 2005, 'duracao': 178},
    2: {'id': 2, 'titulo': 'Sendokai Champions Sengate',       'ano': 2021, 'duracao': 169},
    3: {'id': 3, 'titulo': 'Vingadores: Guerra Infinita',           'ano': 2019, 'duracao': 132},
    4: {'id': 4, 'titulo': 'Miraculous Ladybug Londres',     'ano': 2022, 'duracao': 130},
}
app.config['FILMES'] = FILMES

def obter_filmes():
    return session.get('filmes', [])

def adicionar_filme(titulo):
    filmes = obter_filmes()
    filmes.append(titulo)
    session['filmes'] = filmes

def remover_filme(indice):
    filmes = obter_filmes()
    if 0 <= indice < len(filmes):
        filmes.pop(indice)
        session['filmes'] = filmes

def contar_filmes():
    return len(obter_filmes())

@app.route('/')
# app.py
@app.route('/', methods=['GET', 'POST'])
def filmes():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        if titulo:
            adicionar_filme(titulo)
            flash(f'"{titulo}" adicionado com sucesso!', 'success')
            return redirect(url_for('certo'))
    meus_filmes = obter_filmes()
    quantidade = contar_filmes()
    
    return render_template('index.html', catalogo=app.config['FILMES'], meus_filmes=meus_filmes, quantidade=quantidade)

@app.route('/sucesso')
def certo():
    return render_template('sucesso.html')
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

@app.route('/remover/<int:filme_id>', methods=['POST'])
def remover(filme_id):
    watchlist = session.get('watchlist', [])
    
    if filme_id in watchlist:
        watchlist.remove(filme_id)
        session['watchlist'] = watchlist
        titulo = app.config['FILMES'].get(filme_id, {}).get('titulo', 'Filme')
        flash(f'"{titulo}" removido da sua watchlist.', 'info')
        
    return redirect(url_for('watchlist'))
if __name__ == '__main__':
    app.run(debug=True)