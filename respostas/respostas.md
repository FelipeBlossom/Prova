1 : Explique a diferença entre git merge e git rebase. Qual a vantagem de usar cada um deles? Descreva
um cenário prático onde você escolheria usar rebase ao invés de merge.

O Rebase reproduz as alterações de uma linha de trabalho para outra na ordem em que foram introduzidas, enquanto o Merge é utilizado para a Mescla de Branchs, no caso o rabse pode ser mais indicado quando quiser um histórico de commits mais linear para ser mais limpo.

2: Explique a diferença entre os métodos HTTP GET e POST. Por que é importante usar POST
para envio de formulários que modificam dados no servidor? Dê um exemplo de uma situação
onde GET seria apropriado e outra onde POST seria obrigatório.

O HTTP GET comumente é utilizado como método de requisição para receber informações, uma vez que seu cabeçalho é enviado na url da requisição, enquanto
o método POST é importante de ser utilizado em formulário, uma vez que seu cabeçalho está no body da requisição. Para receber dados o metódo GET pode ser utilizado, mas num envio de dados no formulário melhor ser POST.

3: O que é o objeto request em Flask e para que ele serve? Explique como você pode acessar dados
enviados por: (a) parâmetros de URL (query strings), (b) dados de formulário POST, e (c)
parâmetros dinâmicos na rota. Dê exemplos de código para cada caso.

O objeto request é um objeto global que contém todos as informações para uma requisição POST, como os parametros da URl, dados de formulário, parametros
dinãmicos e outras informações. 
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

Nesse trecho de código é possível perceber  Flask(__name__) cria uma instância de aplicação Flask,e na rota para watchlist está renderizando a página de index passando variáveis como filmes e duracao_total

4: Como funciona o mecanismo de sessões em Flask? Explique onde os dados da sessão são
armazenados (cliente ou servidor) e qual o papel da secret_key nesse processo. Quais são as
limitações de usar sessões para armazenar dados em uma aplicação web?

Os dados da sessão são armazenados no servidor através do uso de cookies, o sacret_key é importante para garantir que seja identificado e garantir que certas ações não autorizadas sejam realizadas. Limitações de usar sessões inclui que ao "perder" a sessão inclui perder todas suas informações, no caso a 
principal limitação de trabalhar com sessão é porque a sessão normalmente possui um tempo limite de expiração, então aplicações com pessoas usando a longo
prazo sentiria uma dificuldade, ou se não deixar a sessão expirar significaria diversos problemas de segurança que se poderia ter.
