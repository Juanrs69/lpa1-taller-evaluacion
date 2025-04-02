# Definimos la clase TipoHabitacion
class TipoHabitacion:
    def __init__(self, tipo, caracteristicas, capacidad_maxima, precio_base, es_activa):
        # Atributos principales de la habitación
        self.tipo = tipo  # Tipo de habitación (Ej: Individual, Doble, Suite)
        self.caracteristicas = caracteristicas  # Lista de características (Ej: TV, WiFi)
        self.capacidad_maxima = capacidad_maxima  # Número máximo de personas
        self.precio_base = precio_base  # Precio por noche
        self.es_activa = es_activa  # Indica si la habitación está disponible
        self.fotos = []  # Lista para almacenar fotos de la habitación

    # Método para agregar fotos a la habitación
    def agregar_foto(self, foto):
        self.fotos.append(foto)
