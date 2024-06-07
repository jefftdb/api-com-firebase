from flask import Flask ,request
import requests

app = Flask(__name__)


"""[
    {
        "id":1,
        "titulo": "O Senhor do Anéis - A sociedade do Anél",
        "Autor": "J.R.R Tolkien"
    },
    {
        "id":2,
        "titulo": "Harry Potter e a Pedra Filosofal",
        "Autor": "J.k Howling"
    },
    {
        "id":3,
        "titulo": "James Clear",
        "Autor": "Hábitos Atômicos"
    }
]"""

#Obter todos
@app.route("/livros", methods =["GET"])
def obter_livros():
    livros = requests.get("https://meu-projeto-7ccc7.firebaseio.com/.json")

    return livros.json()

#Obter livro utilizando o id
@app.route("/livros/<string:id>", methods =["GET"])
def obter_livro_por_id(id):
    livros = requests.get("https://meu-projeto-7ccc7.firebaseio.com/"+ id +".json")

    return livros.json()

#Editar o livro
@app.route("/livros/<string:id>", methods =["PUT"])        
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    requisicao = requests.put("https://meu-projeto-7ccc7.firebaseio.com/"+ id +".json",json = livro_alterado)

    return requisicao.json()
#Criar novo livro
@app.route("/livros", methods =["POST"])
def incluir_novo_livro():
    data = request.get_json()    

    requisicao = requests.post("https://meu-projeto-7ccc7.firebaseio.com/.json",json = data)

    return requisicao.json()

@app.route("/livros/<string:id>", methods =["DELETE"])
def excluir_livro(id):
    requisicao = requests.delete("https://meu-projeto-7ccc7.firebaseio.com/"+ id +".json")
    
    return 'Deletado com sucesso!' 



