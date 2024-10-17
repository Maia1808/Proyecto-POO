
class Controlador:

    def __init__(self):
        self.estado_robot = False
        self.estado_motores = False

    def get_estado_robot(self):
        return self.estado_robot
    
    def conectar_robot(self):
        self.estado_robot = True
        print("Robot conectado.")

    def desconectar_robot(self):
        self.estado_robot = False
        print("Robot desconectado.")

    def get_estado_motores(self):
        return self.estado_motores

    def activar_motores(self):
        self.estado_motores = True
        print("Motores conectados.")
    
    def desactivar_motores(self):
        self.estado_motores = False
        print("Motores desconectados.")