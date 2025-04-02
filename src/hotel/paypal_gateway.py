# Importamos la clase base de pagos
from .pasarela_pago import PasarelaPago

# Definimos la clase PayPalGateway que hereda de PasarelaPago
class PayPalGateway(PasarelaPago):
    # Método para procesar pagos con PayPal
    def procesar_pago(self, monto):
        print(f"Pago de {monto} procesado con PayPal.")

    # Método para reembolsar pagos con PayPal
    def reembolsar_pago(self, monto):
        print(f"Reembolso de {monto} con PayPal.")
