# Definimos la clase Hotel
class Hotel:
    def __init__(self, nombre, direccion, telefono, email, ciudad, estado):
        # Inicializamos los atributos del hotel con la información básica
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.ciudad = ciudad
        self.estado = estado
        self.servicios = []  # Lista para almacenar los servicios del hotel
        self.fotos = []  # Lista para almacenar fotos del hotel

    # Método para registrar un hotel (solo imprime un mensaje en este caso)
    def registrar_hotel(self):
        print(f"Hotel {self.nombre} registrado.")

    # Método para agregar un servicio al hotel
    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    # Método para agregar una foto al hotel
    def agregar_foto(self, foto):
        self.fotos.append(foto)
