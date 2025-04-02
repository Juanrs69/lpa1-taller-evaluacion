# Definimos la clase PasarelaPago (clase base para pagos)
class PasarelaPago:
    # Método genérico para procesar un pago
    def procesar_pago(self, monto):
        print(f"Procesando pago de {monto}...")

    # Método genérico para reembolsar un pago
    def reembolsar_pago(self, monto):
        print(f"Reembolsando {monto}...")
