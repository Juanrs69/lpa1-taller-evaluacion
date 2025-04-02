# Importamos las clases necesarias desde los módulos correspondientes
from hotel.hotel import Hotel
from hotel.servicio import Servicio
from hotel.cliente import Cliente
from hotel.transaccion import Transaccion
from hotel.stripe_gateway import StripeGateway
from hotel.paypal_gateway import PayPalGateway

# --- CREACIÓN DEL HOTEL ---
# Creamos una instancia de la clase Hotel con información ficticia
hotel = Hotel(
    nombre="Hotel Paraiso",
    direccion="Calle 123, Centro",
    telefono="123456789",
    email="contacto@paraiso.com",
    ciudad="Ciudad X",
    estado="Activo"
)

# Mostramos que el hotel ha sido registrado
hotel.registrar_hotel()  # Output: Hotel Paraíso registrado.

# --- AGREGANDO SERVICIOS AL HOTEL ---
# Creamos una instancia de la clase Servicio
servicio_wifi = Servicio("WiFi Gratis")
servicio_piscina = Servicio("Piscina climatizada")

# Agregamos los servicios a la lista de servicios del hotel
hotel.agregar_servicio(servicio_wifi)
hotel.agregar_servicio(servicio_piscina)

# Mostramos los servicios agregados
print("\nServicios del hotel:")
for servicio in hotel.servicios:
    print(f"- {servicio.descripcion}")

# --- REGISTRO DE UN CLIENTE ---
# Creamos un cliente con sus datos personales
cliente1 = Cliente(
    nombre_completo="Juan Perez",
    telefono="5551234567",
    correo="juan@example.com",
    direccion="Avenida Central 456"
)

# Registramos al cliente
cliente1.registrar_cliente()  # Output: Cliente Juan Pérez registrado.

# --- PROCESO DE PAGO USANDO PAYPAL ---
# Creamos una instancia de PayPalGateway para procesar pagos
pago_paypal = PayPalGateway()

# Procesamos un pago de 100 USD con PayPal
pago_paypal.procesar_pago(100.0)  # Output: Pago de 100.0 procesado con PayPal.

# --- PROCESO DE PAGO USANDO STRIPE ---
# Creamos una instancia de StripeGateway para procesar pagos
pago_stripe = StripeGateway()

# Procesamos un pago de 150 USD con Stripe
pago_stripe.procesar_pago(150.0)  # Output: Pago de 150.0 procesado con Stripe.

# --- REGISTRANDO UNA TRANSACCIÓN ---
# Creamos una transacción con los datos del pago realizado
transaccion1 = Transaccion(
    metodo="PayPal",
    monto=100.0,
    estado="Aprobado",
    fecha="2025-04-01"
)

# Mostramos los detalles de la transacción
print("\nDetalles de la transaccion:")
print(f"Metodo: {transaccion1.metodo}")
print(f"Monto: {transaccion1.monto}")
print(f"Estado: {transaccion1.estado}")
print(f"Fecha: {transaccion1.fecha}")
