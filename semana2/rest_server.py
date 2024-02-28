from http.server import HTTPServer
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "Garcia",
        "Carrera": "Ingenieria de sitemas"
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/lista_estudiantes':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(self))

def run_server(port = 8000):
    try:
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        print('Iniciando servidor web en http://localhost:8000/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()

if __name__ == '__main__':
    run_server()