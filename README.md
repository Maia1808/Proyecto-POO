# Proyecto-POO


# Realizado 21/10 Renzo: 

# 1. Clase InterfazServidor
Modificación de la Interfaz:

. Se agregó la opción de seleccionar modo de coordenadas (absolutas o relativas).
. Se actualizó la lista de comandos disponibles para reflejar nuevas opciones.

    Método mostrar_operaciones_cliente:

        . Se implementó para mostrar los comandos G-Code posibles que los clientes u operadores pueden enviar al robot.

    Método seleccionar_modo_coordenadas:

        . Se añadió para cambiar entre coordenadas absolutas (G90) y relativas (G91), y se envía el comando correspondiente al controlador.

    étodo administrar_comandos:

        . Se añadió la lógica para manejar cambios en el modo de trabajo y en el modo de coordenadas.
# 2. Clase Controlador
Manejo de Conexión:

.Se implementaron métodos para conectar y desconectar el robot de manera segura.
.Se aseguró que los parámetros de comunicación (baudrate y puerto COM) se puedan modificar antes de realizar la conexión.

Gestión del Estado:

.Se añadió el seguimiento del estado del robot y de los motores (activados/desactivados).

Envío de Comandos:

. Se implementó el método enviar_comando, que envía comandos al robot y espera recibir una respuesta.
. Se añadió un tiempo de espera de 1 segundo para recibir la respuesta después de enviar un comando.

Manejo de Errores:

. Se mejoró el manejo de errores en el método enviar_comando, incluyendo excepciones específicas relacionadas con la comunicación serie (como SerialTimeoutException y SerialException).
# 3. Nuevas Funciones y Mejoras

Métodos de Encendido y Apagado de Motores:

. Implementados para activar y desactivar los motores del robot mediante comandos G-Code.

. Se incluyeron comandos específicos que los clientes pueden enviar al robot:

M3: Activar gripper
M5: Desactivar gripper
G28: Hacer homing
G1: Movimiento a una posición específica
M114: Reporte de posición actual
G90: Modo de coordenadas absolutas
G91: Modo de coordenadas relativas
M17: Activar motores
M18: Desactivar motores