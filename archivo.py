
class Archivo:
    def __init__(self, estado_conexion: bool, posicion, estado_actividad: str, tiempo: float, ordenes=None):
        self.estado_conexion = estado_conexion  # Estado de la conexión (conectado/desconectado)
        self.posicion = posicion                  # Posición actual del robot
        self.estado_actividad = estado_actividad  # Estado de actividad actual
        self.tiempo = tiempo                      # Tiempo de actividad
        self.ordenes = ordenes if ordenes is not None else []  # Lista de órdenes ejecutadas
        self.cantidad_ordenes = len(self.ordenes)  # Cantidad de órdenes ejecutadas

    def mostrar_info(self):
        "Muestra la información general del archivo."
        print("Estado de conexión:", self.estado_conexion)
        print("Posición del robot:", self.posicion)
        print("Estado de actividad:", self.estado_actividad)
        print("Tiempo de actividad:", self.tiempo)
        print("Órdenes ejecutadas:", self.ordenes)
        print("Cantidad de órdenes ejecutadas:", self.cantidad_ordenes)