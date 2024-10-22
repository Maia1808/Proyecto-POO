from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restringir a un subdirectorio /RPC2
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Crear servidor
with SimpleXMLRPCServer(("127.0.0.1", 8080), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Definir una función remota que el cliente podrá invocar
    def saludo():
        return "¡Conexión exitosa con el servidor XML-RPC!"

    # Registrar la función con el servidor
    server.register_function(saludo, "saludo")

    # Iniciar el servidor
    print("Servidor XML-RPC escuchando en 127.0.0.1:8080...")
    server.serve_forever()