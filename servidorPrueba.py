from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading
import os
import time
import sys

# Restringir a un subdirectorio /RPC2
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Crear servidor
def iniciar_servidor():
    with SimpleXMLRPCServer(("127.0.0.1", 8080), requestHandler=RequestHandler) as server:
        server.register_introspection_functions()

        # Definir una función remota para el saludo personalizado
        def saludo_personalizado(nombre):
            return f"Hola {nombre}, ¡conexión exitosa con el servidor XML-RPC!"

        # Función para apagar el servidor
        def apagar_servidor():
            print("El servidor se está apagando...")
            response = "El servidor se apagará en unos momentos."
            threading.Thread(target=shutdown_servidor, args=(server,)).start()  # Apagar en un hilo separado
            return response

        # Shutdown suave del servidor en otro hilo
        def shutdown_servidor(server):
            time.sleep(1)  # Esperar para dar tiempo al cliente
            server.shutdown()  # Detener el servidor sin forzar la salida
            sys.exit(0)  # Cerrar el programa de manera segura

        # Registrar las funciones con el servidor
        server.register_function(saludo_personalizado, "saludo_personalizado")
        server.register_function(apagar_servidor, "apagar_servidor")

        # Iniciar el servidor
        print("Servidor XML-RPC escuchando en 127.0.0.1:8080...")
        server.serve_forever()

# Iniciar el servidor en un hilo separado
servidor_thread = threading.Thread(target=iniciar_servidor)
servidor_thread.start()