# Práctica 1: Web scraping

### Contexto. Explicar en qué contexto se ha recolectado la información. Explique-por qué el sitio web elegido proporciona dicha información.

Hemos elegido el sitio web [properati.com](https://www.properati.com.ec/) porque se requiere realizar la sifuinte investigación.
__Análisis descriptivo de los anuncios de ventas de casas en el Distrito Metropolitano de Quito - Ecuador.__

Objetivos:
- Calcular el precio aproximado de las casas en venta según el área de las mismas.
- Determinar la variación de los precios en las casas anunciadas según los serctores o barrios en donde se ubican.
- Establecer precios máximos y mínimos de las casas en venta según el número de habitaciones de las mismas.

El sitio web elegido, actualmente consta de las variables necesarias para poder realizar el análisis anteriormente descrito. Las variables extraídas desde la web idicadas se detallan a continuación:

- __Descripción:__ Descripción del anuncio detallando las características del inmueble por parte del venderor.
- __Precio:__ Valor en Dólares del Inmueble.
- __Tipo:__ Variables que describe si inmueble es casa o departamento.
- __Ubicación:__ Dirección del Inmueble.
- __Fecha de publicación:__ Fecha en la que se publicó el anuncio de venta del inmueble.
- __Área:__ Área (en metros cuadrados) del inmueble.
- __Núm. haitaciones:__ Número de habiataciones con las que cuenta el inmueble.

Con las variables definidas se puede cumplir con los objetivos propuestos.

__Objetivo 1.__ Para poder calcular el precio en metros cuadrados vamos a filtrar por sector y posteriormente vamos a determinar el valor de metro cuadrado en función al precio y el área.

__Objetivo 2.__ Podemos sectorizar los precios a través de la variable área y sacando un calculo de la media por sector, tomado de la variable precio.

__Objetivo 3.__ Se filtrará los resultados para calcular el precio máximo y mínimo en función de la variable número de habitaciones.

Actualmente la página web [properati.com](https://www.properati.com.ec/) es una de las más conocidas y demandadas  del país, se encarga de publicar anuncios sobre compra venta y alquiler de varios inmuebles a nivel nacional y actualmente esta pagina o empresa ofrece una aplicación móvil que facilita la navegación y día a día sigue creciendo el numero de personas que accede a ella, para publicar sus diferentes anuncios.
