# Definimos la clase Habitacion
class Habitacion:
    def __init__(self, numero, esta_activo, causa_inactivacion):
        # Atributos principales de la habitación
        self.numero = numero  # Número de la habitación
        self.esta_activo = esta_activo  # Indica si la habitación está en uso
        self.causa_inactivacion = causa_inactivacion  # Motivo si la habitación no está disponible
        self.fotos = []  # Lista para almacenar fotos de la habitación
        self.retroalimentaciones = []  # Lista de opiniones de los clientes

    # Método para agregar fotos a la habitación
    def agregar_foto(self, foto):
        self.fotos.append(foto)

    # Método para agregar comentarios o calificaciones a la habitación
    def agregar_retroalimentacion(self, retroalimentacion):
        self.retroalimentaciones.append(retroalimentacion)
