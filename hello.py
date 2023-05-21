from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, World! </p>"

@app.route("/products")
def products():
    ##transformando em json
    response = jsonify([
        {
            "title":"Caneca Personalizada de Porcelana 123",
            "amount": 123.45,
            "installments": { "number": 6, "total": 41.15, "hasFee": True },
        },
        {
            "title": "Caneca de Tulipa",
            "amount": 123.45,
            "installments": { "number": 3, "total": 41.15 },
        }
    ])

    ##header para efeito de segurança
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response