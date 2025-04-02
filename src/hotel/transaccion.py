# Definimos la clase Transaccion
class Transaccion:
    def __init__(self, metodo, monto, estado, fecha):
        # Atributos de la transacción
        self.metodo = metodo  # Método de pago (Ej: PayPal, Stripe)
        self.monto = monto  # Monto de la transacción
        self.estado = estado  # Estado de la transacción (Ej: Aprobado, Rechazado)
        self.fecha = fecha  # Fecha de la transacción

    # Método para procesar un pago
    def procesar_pago(self):
        print(f"Procesando pago de {self.monto} con {self.metodo}.")

    # Método para reembolsar un pago
    def reembolsar(self):
        print(f"Reembolsando {self.monto} con {self.metodo}.")
