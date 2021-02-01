from registro import *
import random


def carga_automatica():  # CREACION DEL ARCHIVO
    p = random.randint(10, 80)
    archivo_abierto = open(ARCHIVO, "wb")

    for i in range(p):
        titulo = random.choice(NOMBRES_PELICULAS)
        genero = random.randint(0, 5)
        idioma = random.randint(0, 4)
        pelicula = Pelicula(titulo, genero, idioma)
        pickle.dump(pelicula, archivo_abierto)

    archivo_abierto.flush()
    archivo_abierto.close()
    return


if __name__ == '__main__':
    carga_automatica()
    print('El archivo se ha creado con exito!!!')
