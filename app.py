from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {"id": "0",
        "nome": "Gil Xavier",
     "habilidades":["Python", "Flask"]},

    {"id" : "1",
        "nome": "Iury Assunção",
     "habilidades":["JavaScript", "TypeScript"]}
]

@app.route("/dev/<int:id>/", methods= ["GET", "PUT","DELETE"])

def desenvolvedor(id):
    if request.method == "GET":
        
        try:
            response = desenvolvedores[id]
          
        except IndexError:
            mensagem = f"desenvolvedor de ID {id} não existe"
            response = {"status": "erro", "mensagem" : mensagem} 
        except Exception:
            mensagem = "Erro desconhecido, Procure o administrador da API"
            response = {"status": "erro", "mensagem" : mensagem} 
        
        return jsonify (response)
    
    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
        
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({"status": "sucesso!"}, {"mensagem" : "registro excluido!"})


#Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route("/dev/", methods=["POST", "GET"])
def listDevelopers():
    if request.method == "POST":
        dados = json.loads(request.data)
        position = len(desenvolvedores)
        dados["id"] = position
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[position])
        
    elif request.method == "GET":
        return jsonify(desenvolvedores)
        
if __name__ == "__main__":
    app.run(debug=True)