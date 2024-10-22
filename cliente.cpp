#include <iostream>
#include <stdlib.h>
using namespace std;
#include "libreria_Chris_Morley/XmlRpc.h"
using namespace XmlRpc;

int main(int argc, char* argv[])
{
  if (argc != 3) {
    std::cerr << "Uso: cliente IP_HOST N_PORT\n";
    return -1;
  }
  
  int port = atoi(argv[2]);
  
  // Crear el cliente XML-RPC y conectarse al servidor
  XmlRpcClient client(argv[1], port);
  
  XmlRpcValue noArgs, result;

  // Llamar al método 'saludo' en el servidor
  if (client.execute("saludo", noArgs, result))
    std::cout << "Respuesta del servidor: " << result << "\n\n";
  else
    std::cerr << "Error al ejecutar el método 'saludo'\n\n";

  char salida;
  cout << "Ingrese cualquier caracter para salir...";
  cin >> salida;

  return 0;
}
