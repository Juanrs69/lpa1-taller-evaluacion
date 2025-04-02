# SRS proyecto lpa1-taller-requerimientos

## Proyecto Agencia de Viajes

**Autor**: Daniel Andrés Angulo Pérez  
📧 [daniel.angulo.2384@miremington.edu.co]()

---
## Objetivos
- **1:** Definir requisitos funcionales: Especificar las acciones que el sistema debe realizar para gestionar hoteles, habitaciones, reservas y clientes.

- **2:** Establecer requisitos no funcionales: Garantizar rendimiento, seguridad y usabilidad del sistema.

- **3:** Facilitar la experiencia del usuario: Permitir búsquedas intuitivas, reservas seguras y retroalimentación transparente.

---

## Descripcion
**El sistema será una plataforma de reservas de hoteles que permitirá:**

- **Hoteles:** Registrar, gestionar ofertas y mostrar información detallada.

- **Clientes:** Buscar, filtrar y reservar habitaciones con transacciones seguras.

- **Administradores:** Controlar estados (activo/inactivo) y políticas de cancelación.

---

## 📌 Requisitos Funcionales  

A continuación, se detallan los requisitos funcionales del sistema:

| **ID**  | **Requerimiento**                |
|---------|-----------------------------------|
|**RF-001**|EL sistema debe permitir registrar un nuevo hotel con informacion basica como nombre, direccion, telefono, correo electronico, ubicacion geografica|
|**RF-002**|EL sistema debe permitir mostrar una descripcion detallada de los servicios que ofrece el hotel|
|**RF-003**|EL sistema debe permitir mostrar fotos representativas del hotel para que el cliente pueda hacerse una idea|
|**RF-004**|EL sistema debe permitir crear ofertas, como paquetes especiales|
|**RF-005**|EL sistema debe permitir crear descuentos en temporada baja|
|**RF-006**|EL sistema debe permitir crear diferentes habitaciones segun sus caracteristicas|
|**RF-007**|EL sistema debe permitir mostrar fotos de cada habitacion|
|**RF-008**|EL sistema debe permitir tener diferentes condiciones de pago segun el hotel|
|**RF-009**|EL sistema debe permitir tener diferentes politicas de cancelacion, dependiendo del tipo de hotel, habitacion y la temporada|
|**RF-010**|EL sistema debe permitir realizar remmbolsos dependiendo de la politica de cancelacion de cada hotel|
|**RF-011**|EL sistema debe permitir tener un control de actividad/inactividad de cada hotel y debera de mostrar la causa en caso de inactividad|
|**RF-012**|EL sistema debe permitir tener un control de actividad/inactividad de cada habitacion y debera de mostrar la causa en caso de inactividad|
|**RF-013**|EL sistema debe permitir considerar para reservas solo los hoteles y habitaciones que se encuentren en estado de actividad|
|**RF-014**|EL sistema debe permitir hacer un calculo de precio dependiendo los elementos y factores que esten por medio(como capacidad de personas por habitacion o temporada del alojamiento)|
|**RF-015**|EL sistema debe permitir denegar la reserva a una habitacion si la cantidad de personas exede la capacidad maxima|
|**RF-016**|EL sistema debe permitir implementar un calendario regional en los hoteles para analizar las temporadas|
|**RF-017**|EL sistema debe permitir implementar un calendario por habitacion en el que muestre las fechas en las que esta en estado de reserva/disponible|
|**RF-018**|EL sistema debe permitir recibir feedback(calificaciones y comentarios) relacionado a cada habitacion|
|**RF-019**|EL sistema debe permitir hacer un promedio entre el feedback de cada habitacion para sacar una calificacion general para el hotel|
|**RF-020**|EL sistema debe permitir registrar a un cliente con informacion basica como nombre completo, telefono, correo, direccion|
|**RF-021**|EL sistema debe permitir realizar busquedas de parte del cliente de hoteles y habitaciones y filtrar busquedas como fecha, ubicacion, calificacion, precio|
|**RF-022**|EL sistema debe permitir que el cliente pueda ver detalles de las habitaciones como servicios incluidos, fotos, feedback|
|**RF-023**|EL sistema debe permitir revisar y confirmar la transaccion por parte del cliente|

---

## 🔒 Requisitos No Funcionales  

A continuación, se presentan los requisitos no funcionales del sistema:

---

| **ID**  | **Requerimiento**                |
|---------|-----------------------------------|
|**RNF-001**|EL sistema debe permitir manejar muchas reservas simultáneas|
|**RNF-002**|EL sistema debe permitir cifrar datos sensibles |
|**RNF-003**|EL sistema debe permitir tener compatibilidad con APIs de pasarelas de pago |