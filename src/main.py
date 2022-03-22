from flask import Flask, request

app = Flask(__name__)
app.config['JSON_ASS_ASCII'] = False

#estrutura simples para simular fonte de dados.
users_data = {
    1: {
        "id": 1,
        "nome": "Roberto"
    },
    2: {
        "id": 2,
        "nome": "Marcao"
    }
}

def responseUsers():
    return {"users": list(users_data.values())}

@app.route("/")
def root():
    return "Bem-vindo =D"

#retorna todos usuários contidos na fonte.
@app.route("/users")
def listUsers():
    return responseUsers()

#metodo insere novos usuários no objeto automaticamente com novo id.
@app.route("/users", methods=['POST'])
def newUser():
    body = request.json

    ids = list(users_data.keys())

    if ids:
        new_id = ids[-1] + 1
    else:
        new_id = 1

    users_data[new_id] = {
        "id": new_id,
        "nome": body["name"]
    }
    return responseUsers()

#Realiza a exclusão do usuário por ID
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete(user_id: int):
    user = users_data.get(user_id)

    if user:
        del users_data[user_id]

    return responseUsers()

#realiza a atualização do usuário assim que inserir a nova info.
@app.route("/users/<int:user_id>", methods = ["PUT"])
def update(user_id: int):
    body = request.json
    name = body.get("name")

    if user_id in users_data:
        users_data[user_id]["name"] = name

    return responseUsers()

app.run(debug=True)
