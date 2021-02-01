Se solicita un pequeño sistema para administrar las películas de una videoteca. Las películas deben almacenarse en un archivo binario “peliculas.dat”. El registro a almacenar en el archivo debe poseer la siguiente información de cada película:

Título o nombre.
Género: 0-Infantil, 1-Comedia, 2-Romántico, 3-Drama, 4-Ciencia Ficción, 5-Otros.
Idioma Original: 0-Español, 1: Inglés, 2: Francés, 3: Portugués, 4:Otros.
Se debe desarrollar un módulo que sirva para generar el archivo binario “peliculas.dat” con datos de manera aleatoria.

Y por otra parte, se pide un programa controlado por menú de opciones que permita:

 1 A partir del archivo generar un vector con todas las películas. Mostrar el vector a razón de una línea por película mostrando el género y el idioma en lugar de sus códigos) ordenado por título (utilizando la inserción ordenada).
 2 A partir del vector generar una lista de n películas (n se ingresa por teclado) que sean del género g (g se ingresa por teclado). Si no hubiera suficientes películas del género ingresado, generar la lista con los que haya e informar con un mensaje. Mostrar la lista generada.
 3 A partir del vector determinar la cantidad de películas por género y por idioma. Para eso se debe utilizar una matriz de conteo. Mostrar las cantidades sólo cuando sean mayores a 0. Se debe mostrar el nombre del idioma y del género y no sus códigos.
 4 A partir de la matriz determinar la cantidad de películas para el idioma i, siendo i un valor ingresado por teclado.
 5 Buscar en el vector una película con el título x (x se ingresa por teclado). Si la película existe, mostrar sus datos. Si no, informar con un mensaje.
 6 Ingresar por teclado un idioma x. Generar un archivo de texto cuyo nombre tenga la forma “PeliculasIdiomax.txt” (reemplazando x por el número del idioma seleccionado) conteniendo todas las películas de ese idioma.

Se debe validar en toda situación posible.


Para iniciar el programa, ejecute el archivo Principal.py