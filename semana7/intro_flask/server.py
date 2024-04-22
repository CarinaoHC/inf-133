from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

@app.route("/saludar", methods=["GET"])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

@app.route("/sumar", methods=["GET"])
def sumar():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    if not num1 and num2:
        return (
            jsonify({"error": "Se requiere un numero en los parámetros de la URL."}),
            400,
        )
    suma = int(num1) + int(num2)
    return jsonify({"mensaje": f"{'La suma es :', suma}"})

@app.route("/palindromo", methods=["GET"])
def palindromo():
    cadena = request.args.get("cadena")
    if not cadena:
        return (
            jsonify({"error": "Se requiere una cadena en los parámetros de la URL."}),
            400,
        )
    x=cadena.lower()  
    y=''.join(reversed(x))
    return jsonify({"mensaje": f"{'Es un Palíndromo' if (y==x) else 'No es un Palíndromo'}"})

@app.route("/contar", methods=["GET"])
def contar():
    cadena = request.args.get("cadena")
    vocal = request.args.get("vocal")
    if not cadena and vocal:
        return (
            jsonify({"error": "Se requiere una cadena en los parámetros de la URL."}),
            400,
        )
    res = map(cadena.lower().count, vocal)
    return jsonify({"mensaje": f"{'La suma es :', res}"})


if __name__ == "__main__":
    app.run()