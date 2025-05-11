from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from auth import getToken
from query_service import buscarBaterias
from output import criarMensagem

app = Flask(__name__, template_folder="templates")
CORS(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api/baterias', methods=['GET'])
def baterias():
    email = request.args.get('email')
    if not email:
        return jsonify({'erro': 'E-mail não fornecido'}), 400
    try:
        token = getToken()
        baterias = buscarBaterias(token, email)
        mensagem, passadas = criarMensagem(baterias)
        return jsonify({'mensagem': mensagem, 'passadas': passadas})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
