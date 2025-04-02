# Definimos la clase Retroalimentacion
class Retroalimentacion:
    def __init__(self, calificacion, comentario, fecha):
        # Atributos principales de la retroalimentación
        self.calificacion = calificacion  # Puntuación del 1 al 5
        self.comentario = comentario  # Comentario del cliente
        self.fecha = fecha  # Fecha en que se dejó la retroalimentación
