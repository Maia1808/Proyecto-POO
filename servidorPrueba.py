from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import sys

# Restringir a un subdirectorio /RPC2
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Crear servidor
with SimpleXMLRPCServer(("127.0.0.1", 8080), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Definir una función remota para el saludo personalizado
    def saludo_personalizado(nombre):
        return f"Hola {nombre}, ¡conexión exitosa con el servidor XML-RPC!"

    # Función para apagar el servidor
    def apagar_servidor():
        print("El servidor se está apagando...")
        server.server_close()
        sys.exit()

    # Registrar las funciones con el servidor
    server.register_function(saludo_personalizado, "saludo_personalizado")
    server.register_function(apagar_servidor, "apagar_servidor")

    # Iniciar el servidor
    print("Servidor XML-RPC escuchando en 127.0.0.1:8080...")
    server.serve_forever()
