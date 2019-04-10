'''
Practica 1: Web web_scraping
Responsables:
 DIEGO CASTILLO CARRION
 CARLOS HERNANDEZ MARTINEZ

Descripcion:
Se realiza el ejercicio de web web_scraping sobre la web: properati.com
en donde se trata de obtener la principal informacion de los anuncions de
ventas de casas en Quito - Ecuador.

Fecha de ejecucion:
06.04.2019
'''

# Se importan las librerias necesarias
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

# Contador que representa el número de página
numPagina = 1

# Gestion del archivo csv
fileName = "casas.csv"
f = open(fileName,"w")
encabezado = "descripcion|precio|tipo|ubicacion|fecha_publicacion|area|num_habitaciones\n"
f.write(encabezado)

# El while permite navegar por las paginas de la web
# Se gestionan tambien las exepciones que se podrian dar
while numPagina <= 20:
    try:
        html = urlopen('https://www.properati.com.ec/pichincha-ecuador/quito/casa/venta/'+str(numPagina)+'/')
    except HTTPError as err:
        print(err)
    except URLError:
        print('El servidor está caido o el dominio es incorrecto')
    else:
        if res.title is None:
            print("Tag no encontrado")
        else:
            res = BeautifulSoup(html.read(),'html5lib')
            tags = res.findAll("article",{"class":"item"})

            for tag in tags:

                # Se obtiene la descripcion del anuncio
                contenedorDescripcion = tag.findAll("a",{"class":"item-url"})
                desc = contenedorDescripcion[0].text.strip()
                print(desc)

                # Se obtiene el precio del inmueble
                contenedorPrecio = tag.findAll("p",{"class":"price"})
                precio = contenedorPrecio[0].text.strip()
                print(precio)

                # Se obtiene el tipo de inmueble
                contenedorTipo = tag.findAll("p",{"class":"property-type"})
                tipo = contenedorTipo[0].text.strip()
                print(tipo)

                # se obtiene la Ubicacion del inmueble
                contenedorUbicacion = tag.findAll("p",{"class":"location"})
                ubicacion = contenedorUbicacion[0].text.strip()
                print(ubicacion)

                # Fecha de publicacion
                contenedorFecha = tag.findAll("p",{"class":"date-added"})
                fecha = contenedorFecha[0].text.strip()
                print(fecha)

                # Area del inmueble, algunos valores vienen vacios
                # por lo que se llenan con ''
                contenedorHabitaciones = tag.findAll("p",{"class":"rooms"})
                if len(contenedorHabitaciones) > 0:
                    TagArea = contenedorHabitaciones[0].find('span')
                    if TagArea != None:
                        area = TagArea.text.strip()
                    else:
                        area = ''
                else:
                    area = ''
                print(area)

                # Numero  de habitaciones. Algunos valores vienen vacios
                # y se llenan con ''
                if len(contenedorHabitaciones) > 0:
                    tagNoDeseado = contenedorHabitaciones[0].find('span')
                    if tagNoDeseado != None:
                        tagNoDeseado.extract()
                        habitaciones = contenedorHabitaciones[0].text.strip()
                    else:
                        habitaciones = contenedorHabitaciones[0].text.strip()
                else:  habitaciones = ''
                print(habitaciones)

                # Se escriben los datos en el rchivo csv
                f.write(desc+"|"+precio+"|"+tipo+"|"+ubicacion+"|"+fecha+"|"+area+"|"+habitaciones+"\n")

    numPagina += 1

f.close()
