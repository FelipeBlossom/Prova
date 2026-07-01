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

@app.route('/', methods=['GET', 'POST'])
def filmes():
    if request.method == 'POST':

        # Cadastro de um novo filme
        if request.form.get("titulo"):
            titulo = request.form.get("titulo")
            ano = int(request.form.get("ano"))
            duracao = int(request.form.get("duracao"))

            novo_id = max(app.config["FILMES"].keys()) + 1

            app.config["FILMES"][novo_id] = {
                "id": novo_id,
                "titulo": titulo,
                "ano": ano,
                "duracao": duracao
            }

            flash(f'"{titulo}" cadastrado com sucesso!', "success")

        # Adicionar filme existente à watchlist
        elif request.form.get("filme_id"):
            filme_id = int(request.form.get("filme_id"))

            watchlist = session.get("watchlist", [])

            if filme_id not in watchlist:
                watchlist.append(filme_id)
                session["watchlist"] = watchlist

                flash(
                    f'"{app.config["FILMES"][filme_id]["titulo"]}" adicionado à watchlist!',
                    "success"
                )
            else:
                flash("Esse filme já está na watchlist.", "warning")

        return redirect(url_for("filmes"))

    # ======== GET ========
    watchlist_ids = session.get('watchlist', [])
    filmes_watchlist = []
    duracao_total = 0

    for filme_id in watchlist_ids:
        if filme_id in app.config['FILMES']:
            filme = app.config['FILMES'][filme_id]
            filmes_watchlist.append(filme)
            duracao_total += filme['duracao']

    return render_template(
        'index.html',
        filmes=app.config['FILMES'],
        filmes_watchlist=filmes_watchlist,
        duracao_total=duracao_total
    )

@app.route('/sucesso')
def certo():
    return render_template('sucesso.html')

@app.route('/watchlist')
def watchlist():
    watchlist_ids = session.get('watchlist', [])
    filmes_watchlist = []
    duracao_total = 0

    for filme_id in watchlist_ids:
        if filme_id in app.config['FILMES']:
            filme = app.config['FILMES'][filme_id]
            filmes_watchlist.append(filme)
            duracao_total += filme['duracao']

    return render_template(
        'index.html',
        filmes=app.config['FILMES'],
        filmes_watchlist=filmes_watchlist,
        duracao_total=duracao_total
    )

@app.route('/remover/<int:filme_id>', methods=['POST'])
def remover(filme_id):
    watchlist = session.get('watchlist', [])

    if filme_id in watchlist:
        watchlist.remove(filme_id)
        session['watchlist'] = watchlist

        titulo = app.config['FILMES'][filme_id]['titulo']
        flash(f'"{titulo}" removido da sua watchlist.', 'info')

    return redirect(url_for('filmes'))

if __name__ == '__main__':
    app.run(debug=True)