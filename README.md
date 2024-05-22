# Proyecto Final CoderHouse 2024
**Comisión:** 54135

**Alumna:** Emma Fuhr

ENLACE VIDEO EXPLICATIVO: https://drive.google.com/file/d/1xG1GBOfl4gU5u0lmlDLB_SMsn7MfSNDg/view?usp=drive_link

## Acerca del Proyecto

Esta aplicación web está diseñada para la gestión de pedidos en una empresa de venta de artículos de perfumería. La aplicación permite a los usuarios gestionar pedidos realizados por vendedores, controlar el stock de artículos y gestionar el registro de clientes. Además, cuenta con un módulo de administración donde un superusuario, "admin", puede dar de alta a nuevos usuarios de la empresa. La aplicación también es accesible al público con funciones restringidas, permitiendo solo la visualización de la página de inicio, los artículos disponibles y la sección "About".

## Aplicaciones

- **Core:** Pantalla principal que sirve como punto de entrada a la aplicación.
  
- **Cliente:** Permite la visualización y gestión de clientes registrados, incluyendo el ingreso de nuevos clientes.
  
- **Artículo:** Permite la visualización y gestión de artículos disponibles, incluyendo la carga de nuevos artículos.
  
- **Pedido:** Permite la visualización y gestión de pedidos registrados, incluyendo la creación de nuevos pedidos.
  
- **Vendedor:** Permite la visualización y gestión de vendedores registrados, permitiendo al administrador crear nuevos vendedores.

## Modelos

Las aplicaciones mencionadas utilizan los siguientes modelos para gestionar la información:

- **Cliente:** Almacena datos de clientes, incluyendo nombre, apellido, DNI, fecha de nacimiento, dirección, ciudad y avatar.
  
- **Artículo:** Almacena datos de artículos, incluyendo nombre, descripción, precio, stock, fecha de actualización e imagen del producto.
  
- **Pedido:** Almacena datos de pedidos, incluyendo vendedor, cliente, artículo, cantidad, total de venta y fecha de creación.
  
- **Vendedor:** Almacena datos de vendedores, incluyendo nombre, teléfono, ciudad, fecha de alta y avatar.

## Funcionalidades

- **Gestión de Clientes:** Registro y administración de clientes con toda la información relevante.
  
- **Gestión de Artículos:** Registro y administración de artículos con detalles como descripción, precio y stock.
  
- **Gestión de Pedidos:** Creación y administración de pedidos, vinculando clientes, artículos y vendedores.
  
- **Control de Stock:** Monitoreo y actualización del stock de artículos disponibles.
  
- **Administración de Usuarios:** El superusuario "admin" tiene la capacidad de crear y gestionar usuarios dentro de la empresa.
  
- **Acceso Público Restringido:** Los visitantes pueden acceder a la página de inicio, ver los artículos disponibles y la sección "About" sin necesidad de autenticarse.

## Acceso y Roles de Usuario

- **Superusuario ("admin"):** Tiene acceso completo a todas las funcionalidades de la aplicación, incluyendo la administración de usuarios.
  
- **Vendedores:** Pueden gestionar sus propios pedidos y ver la información relacionada con los clientes y artículos.
  
- **Clientes Registrados:** Pueden ver y gestionar sus propios pedidos.
  
- **Público:** Puede acceder a la página de inicio, ver los artículos disponibles y la sección "About" con funciones limitadas.


