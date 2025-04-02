# Definimos la clase Cliente
class Cliente:
    def __init__(self, nombre_completo, telefono, correo, direccion):
        # Atributos principales del cliente
        self.nombre_completo = nombre_completo
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    # Método para registrar a un cliente (simula un registro con un mensaje)
    def registrar_cliente(self):
        print(f"Cliente {self.nombre_completo} registrado.")
