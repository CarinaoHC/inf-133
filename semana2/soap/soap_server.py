from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler


def saludar(nombre):
    return "¡hola, {}!".format(nombre)


def sumaDosNumeros(num1, num2):
    return num1 + num2


def cadenaPalindromo(cadena):
    return "¡hola, {}!".format(cadena)


dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    "CadenaPalindromo",
    cadenaPalindromo,
    returns={"saludo": str, "cadenaPalindromo": str},
    args={"nombre": str, "cadena": str},
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciando en http://localhost:8000/")
server.serve_forever()
