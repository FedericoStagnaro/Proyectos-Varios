from funciones import *


def menu():
    print("------------------------------------------------------------------------------------")
    print("(0)Generar el archivo.")
    print("(1)Mostrar lista de peliculas, ordenado por titulo(del archivo).")
    print("(2)A partir del vector,mostrar (N) pelis,del genero (G) y mostrar.")
    print("(3)Determinar cantidad de peliculas Genero/Idioma.Mostrar mayores a 0.")
    print("(4)Determinar cantidad de peliculas del idioma (I).")
    print("(5)Buscar en el vector la pelicula con el titulo (X).")
    print("(6)Generar archivo de texto ,Idioma (X).")
    print("(7)Salir")
    print("-------------------------------------------------------------------------------------")


def test():
    op = -1

    peliculas = []
    matriz = []

    while op != 7:
        menu()
        op = validar_int_entre(0, 7, "Ingrese una opcion valida:")

        if op == 0:
            carga_automatica()
            print("Archivo generado.")
        if op == 1:
            if os.path.exists(ARCHIVO):  # Generar y mostrar lista de peliculas, ordenado por titulo(del archivo)
                peliculas = lectura_binario()
                leer_vector(peliculas)
            else:
                print("El archivo no existe o no se ha encontrado...Por favor Ingrese a la opcion 0.")

        elif op == 2:
            if not peliculas:
                print("Aun no se han cargado las peliculas, ingrese a la opcion uno.")
            else:
                opcion_2(peliculas)

        elif op == 3:
            if not peliculas:
                print("Aun no se han cargado las peliculas, ingrese a la opcion uno.")
            else:
                matriz = generar_matriz()
                cargar_matriz(matriz, peliculas)
                lectura_matriz(matriz)

        elif op == 4:
            if not matriz:
                print("Aun no se han cargado las peliculas en la matriz de conteo, ingrese a la opcion tres.")
            else:
                consultar_cantidad(matriz)

        elif op == 5:
            if not peliculas:
                print("Aun no se han cargado las peliculas, ingrese a la opcion uno.")
            else:
                busqueda_titulo(peliculas)

        elif op == 6:
            if not peliculas:
                print("Aun no se han cargado las peliculas, ingrese a la opcion uno.")
            else:
                seleccion_idioma(peliculas)


if __name__ == '__main__':
    test()
