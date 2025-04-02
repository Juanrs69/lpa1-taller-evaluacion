# Importamos la clase base de pagos
from .pasarela_pago import PasarelaPago

# Definimos la clase StripeGateway que hereda de PasarelaPago
class StripeGateway(PasarelaPago):
    # Método para procesar pagos con Stripe
    def procesar_pago(self, monto):
        print(f"Pago de {monto} procesado con Stripe.")

    # Método para reembolsar pagos con Stripe
    def reembolsar_pago(self, monto):
        print(f"Reembolso de {monto} con Stripe.")
