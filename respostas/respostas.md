1 : Explique a diferença entre git merge e git rebase. Qual a vantagem de usar cada um deles? Descreva
um cenário prático onde você escolheria usar rebase ao invés de merge.

O git Rebase reproduz as alterações de uma linha de trabalho para outra na ordem em que foram introduzidas, ou seja, o git Rebase usa as alterações feitas em outra branch e cria um histórico linear como se aquelas alterações tivessem sido feitas originalmente por aquela branch. Enquanto o Merge é utilizado para a mescla de Branchs, como também cria um novo commit de merge e permanecendo o histórico original da Branch. A vantagem do Rebase está relacionado a um histórico mais limpo, enquanto o Merge manter todo o histórico. Uma rebase poderia ser utilizado antes de um pull request se for necessário atualizar com o remoto.

2: Explique a diferença entre os métodos HTTP GET e POST. Por que é importante usar POST
para envio de formulários que modificam dados no servidor? Dê um exemplo de uma situação
onde GET seria apropriado e outra onde POST seria obrigatório.

O HTTP GET comumente é utilizado como método de requisição para receber informações, uma vez que seus parâmeotros é enviado na url da requisição, como para consultas e pesquisas, enquanto
o método POST é importante de ser utilizado em formulário, uma vez que seus parâmetros estão no body da requisição, ou seja, evitando informações expostas na URL. Pode ser utilizado para um cadastro de um filme ou para envios de formulários

3: O que é o objeto request em Flask e para que ele serve? Explique como você pode acessar dados
enviados por: (a) parâmetros de URL (query strings), (b) dados de formulário POST, e (c)
parâmetros dinâmicos na rota. Dê exemplos de código para cada caso.

O objeto request é um objeto global que contém todas as informações para uma requisição HTTP, ele permite
informações enviadas pelo cliente, dados de formulários, cookies, entre outras informações de requisição.

por parâmetros de url (query strings) usa-se request.args.get("elemento"), então na URL de uma rota como filtro por exemplo buscaria
/filtrar?elemento=senhor, então  request.args.get("elemento") retorna "senhor"

por dados de formulário POST request.form.get ("campo"), então utiliza-se para acesasr os valores enviados no corpo da requisição
Exemplo:  
    @app.route("/cadastro", methods=["POST"])
    def cadastro():
        nome = request.form.get("nome")
Caso o formulário envie um campo que se chama nome, então essa variável nome irá receber esse valor

por paramêtros dinâmicos da rota são usados para alterar dinamicamente na própria URl da rota e ser recebido como parâmetro da função daquela rota em específica
@app.route('/adicionar/<int:filme_id>', methods=['POST'])
def adicionar(filme_id):
    return str((filme_id))
caso a URL for /adicionar/4, então a variável filme_id será 4

4: Como funciona o mecanismo de sessões em Flask? Explique onde os dados da sessão são
armazenados (cliente ou servidor) e qual o papel da secret_key nesse processo. Quais são as
limitações de usar sessões para armazenar dados em uma aplicação web?

Os dados da sessão são armazenados no cliente através do uso de cookies, a secret_key é usada para assinar o cookie e garantir a integridade do cookie da sessão que caso tenha uma alteração, o Flask detecte a alteração, suas limitações de usar sessões inclui que ao "perder" a sessão inclui perder todas suas informações, no caso a 
principal limitação de trabalhar com sessão é porque a sessão normalmente possui um tempo limite de expiração, então aplicações com longo prazo precisaria que o usuário logasse novamente.
