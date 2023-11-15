from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Algoritmos - Teoria e Prática',
        'autor': 'Thomas H. CormenThomas H. Cormen'
    },
    {
        'id': 2,
        'titulo': 'Perfeitamente Proibido',
        'autor': 'T M Kechichian'
    },
    {
        'id': 3,
        'titulo': 'Diário de um Banana 1',
        'autor': 'Jeff Kinney'
    }
]


# Obter todos os livros
@app.route('/livros', methods=['GET'])

def obter_livros():
    return jsonify(livros)


# Obter livro por ID
@app.route('/livros/<int:id>', methods=['GET'])

def obter_livros_ID(id):
    for livro in livros:
        if livro.get('id') == id: 
            return jsonify(livro);

# Atualizar livro por ID
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livros(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
# Incluir livro por ID
@app.route('/livros', methods=['POST'])
def incluir_livro():
    novo_livro =request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Excluir livro por ID
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros [indice]

        return jsonify(livros)
        
app.run(port=5000,host='localhost', debug=True)