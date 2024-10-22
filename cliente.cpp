#include <iostream>
#include <stdlib.h>
using namespace std;
#include "libreria_Chris_Morley/XmlRpc.h" 
using namespace XmlRpc;

void mostrarMenu() {
    cout << "Menu de opciones:\n";
    cout << "1. Saludo personalizado\n";
    cout << "2. Salir y apagar todo\n";
    cout << "Seleccione una opción: ";
}

int main(int argc, char* argv[])
{
  if (argc != 3) {
    std::cerr << "Uso: cliente IP_HOST N_PORT\n";
    return -1;
  }
  
  int port = atoi(argv[2]);
  XmlRpcClient client(argv[1], port);
  XmlRpcValue result, noArgs, args;

  int opcion;
  
  while (true) {
    mostrarMenu();
    cin >> opcion;

    if (opcion == 1) {
      // Solicitar saludo personalizado
      string nombre;
      cout << "Ingrese su nombre para el saludo personalizado: ";
      cin >> nombre;
      args[0] = nombre;

      if (client.execute("saludo_personalizado", args, result))
        std::cout << "Respuesta del servidor: " << result << "\n\n";
      else
        std::cerr << "Error al ejecutar el saludo personalizado\n\n";
    }
    else if (opcion == 2) {
      // Apagar el servidor y salir
      if (client.execute("apagar_servidor", noArgs, result))
        std::cout << "Servidor apagado correctamente.\n\n";
      else
        std::cerr << "Error al intentar apagar el servidor.\n\n";

      cout << "Cliente apagado.\n";
      break;
    }
    else {
      cout << "Opción inválida. Intente de nuevo.\n";
    }
  }

  return 0;
}
