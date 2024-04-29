# Proyecto CoderHouse
Comisión: 54135

Alumna: Emma Fuhr

## Acerca del Proyecto
Esta aplicación web está orientada a la venta de artículos exclusivos de perfumería. Cuenta con un registro de Clientes y Artículos, como también la gestión de pedidos realizados por cada cliente. Estos módulos facilitan la obtención de información para cada proceso de compra.


## Tecnologías utilizadas en el proyecto
    asgiref 3.8.1    Django 5.0.4    sqlparse 0.5.0    tzdata 2024.1


## Aplicaciones    
    Core: Pantalla principal  
      
    Cliente: Muestra los clientes registrados y permite el ingreso de nuevos clientes.

    Artículo: Muestra los artículos disponibles y permite la carga de nuevos artículos.

    Pedido: Muestra los pedidos registrados y permite la creación de nuevos pedidos.

### Modelos
Las aplicaciones anteriores utilizan el contenido de los siguientes modelos:

    -Cliente: Almacena todos los datos correspondientes de cada cliente: nombre, apellido, DNI, dirección y ciudad.

    -Artículo: Almacena todos los datos correspondientes a cada artículo: nombre, descripción y precio.

    -Pedido: Almacena todos los datos correspondientes a cada pedido: cliente, artículo y cantidad.

## Mejoras futuras

Las mejoras para el proyecto en un futuro son las detalladas a continuación:

-Agregar una app de carrito para gestionar la venta     

-Agregar en base de datos las imágenes de producto de los artículos registrados para que cuando se ingresa a la app Artículos permita ver junto a la descripción, la foto del artículo en cuestión.    

-Agregar en la página principal una sección donde cada cliente puede detallar su experiencia con la tienda.    

-Modificar la forma en la que se muestra al público en general, ya que en este caso cualquiera tiene acceso a toda la información de la tienda. Se necesita crear usuario de gestión de los propietarios de la tienda, los cuales tendrán el acceso a toda la información. Y luego crear la visual de cliente la cual únicamente permite registrarse para realizar compras y gestionar sus propios pedidos.