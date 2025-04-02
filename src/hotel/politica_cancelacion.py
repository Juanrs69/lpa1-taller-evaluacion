# Definimos la clase PoliticaCancelacion
class PoliticaCancelacion:
    def __init__(self, terminos, condiciones):
        # Atributos que almacenan términos y condiciones de cancelación
        self.terminos = terminos
        self.condiciones = condiciones

    # Método que simula el cálculo de reembolso para una reserva
    def calcular_reembolso(self, reserva):
        print(f"Calculando reembolso para la reserva {reserva}")
