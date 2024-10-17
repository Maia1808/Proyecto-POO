from archivo import Archivo
from logTrabajo import LogTrabajo
from servidor import Servidor
from controlador import Controlador

class InterfazServidor:

    def __init__(self, modo_trabajo = "automatico"):
        self.modo_trabajo = modo_trabajo

    def listar_comandos(self):
        print("Comandos posibles a realizar: \n")
        print(" 1) Conectar/desconectar robot. \n")
        print(" 2) Activar/desactivar motores del robot. \n")
        print(" 3) Mostrar reporte de informacion general. \n")
        print(" 4) [SOLO ADMIN] Mostrar reporte de log de trabajo del servidor. \n")
        print(" 5) Seleccionar los modos de trabajo (manual o automatico). \n")
        print(" 6) [SOLO ADMIN] Mostrar usuarios. \n")
        print(" 7) [SOLO ADMIN] Mostrar/editar los parametros de conexion del robot. \n")
        print(" 8) [SOLO ADMIN] Encender/apagar servidor. \n")
        print(" 9) Mostrar operaciones posibles a realizar por un CLIENTE. \n")

    def administrar_comandos(self):
        opcion_elegida = None
        while opcion_elegida not in list(range(1,10)):
            try:
                opcion_elegida = int(input("Ingrese la acción a realizar: "))
                if opcion_elegida == 1:
                    self.activar_desactivar_robot()
                elif opcion_elegida == 2:
                    self.activar_desactivar_motores()
                elif opcion_elegida == 3:
                    self.mostrar_reporte_general()
                elif opcion_elegida == 4:
                    self.mostrar_log_trabajo()
                elif opcion_elegida == 5:
                    self.seleccionar_modo_trabajo()
                elif opcion_elegida == 6:
                    self.mostrar_usuarios()
                elif opcion_elegida == 7:
                    self.mostrar_parametros_conexion()
                elif opcion_elegida == 8:
                    estado_servidor = Servidor.get_estado_servidor()
                    if estado_servidor == True:
                        Servidor.iniciar_servidor()
                    else:
                        Servidor.apagar_servidor()
                elif opcion_elegida == 9:
                    self.mostrar_operaciones_cliente()
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
            

    def activar_desactivar_robot(self):
        if Controlador.get_estado_robot() == True:
            Controlador.desconectar_robot()
        else:
            Controlador.conectar_robot()

    def activar_desactivar_motores(self):
        if Controlador.get_estado_motores() == True:
            Controlador.desconectar_motores()
        else:
            Controlador.conectar_motores()

    def mostrar_reporte_general(self):
        Archivo.mostrar_info()

    def mostrar_log_trabajo(self):
        self.sesion = Servidor.get_sesion()
        self.usuario = Servidor.get_usuarios()
        if self.sesion and 'nombre_usuario' in self.sesion:
            nombre_usuario = self.sesion['nombre_usuario']
            # Verificamos si el usuario tiene permisos de administrador
            for usuario in self.usuarios:
                if usuario.nombre_usuario == nombre_usuario and usuario.admin:
                    LogTrabajo.leer_CSV()
                    return
            print("Acceso denegado. Solo los administradores pueden ver la lista de usuarios.")
        else:
            print("No hay ningún usuario en sesión.")

    def seleccionar_modo_trabajo(self):
        self.modo_trabajo = None
        while self.modo_trabajo not in "manual" or "automatico":
            self.modo_trabajo = input("Ingrese: manual/automatico")
        print(f"Modo de trabajo en {self.modo_trabajo}")

    def mostrar_usuarios(self):
        self.sesion = Servidor.get_sesion()
        self.usuario = Servidor.get_usuarios()
        if self.sesion and 'nombre_usuario' in self.sesion:
            nombre_usuario = self.sesion['nombre_usuario']
            # Verificamos si el usuario tiene permisos de administrador
            for usuario in self.usuarios:
                if usuario.nombre_usuario == nombre_usuario and usuario.admin:
                    print("Usuarios registrados:")
                    for u in self.usuarios:
                        print(u.nombre_usuario)  # Muestra el nombre del usuario
                    return
            print("Acceso denegado. Solo los administradores pueden ver la lista de usuarios.")
        else:
            print("No hay ningún usuario en sesión.")

    def modificar_parametros_conexion(self):
        # ESCRIBIR CODIGO PARA MODIFICAR PARAMETROS
        pass

    def mostrar_operaciones_cliente(self):
        # ESCRIBIR CODIGO PARA MOSTRAR OPERACIONES CLIENTE
        pass

    

    