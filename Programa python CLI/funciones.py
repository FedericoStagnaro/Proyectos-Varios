from archivos import *


def validar_int_entre(desde, hasta, mensaje):
    flag = False
    while not flag:
        num = int(input(mensaje))
        if desde <= num <= hasta:
            return num
        else:
            print("El valor ingresado no se encuentra comprendido entre", desde, "y", hasta, ". Vuelva a intentar.")


def validar_int_mayorigual(desde, mensaje):
    flag = False
    while not flag:
        num = int(input(mensaje))
        if num >= desde:
            return num
        else:
            print("El valor ingresado no es mayor o igual que", desde, ". Vuelva a intentar.")


def opcion_2(vector):  # A partir del vector, mostrar (N) pelis,del genero (G) y mostrar.
    print("-------------------------------------------------------------------------------------")
    n = validar_int_mayorigual(1, "Ingrese el numero de peliculas que desea visualizar:")
    g = validar_int_entre(1, 6, "Ingrese el genero de las peliculas que desea visualizar:"
                                "\n(1)Infantil\n(2)Comedia\n(3)Romántico\n(4)Drama\n(5)Ciencia Ficción\n(6)Otros")
    print("-------------------------------------------------------------------------------------")
    peliculas_x_genero = []
    g -= 1
    for i in range(len(vector)):
        if vector[i].genero == g:
            peliculas_x_genero.append(vector[i])
        if len(peliculas_x_genero) == n:
            break

    if not peliculas_x_genero:
        print("No se han encontrado peliculas con las descripcion sugerida.")
        return
    elif len(peliculas_x_genero) < n:
        print("Solo se han encontrado:", len(peliculas_x_genero), " de ", n, " peliculas solicitadas del genero",
              GENERO[g])

    print('Lista de peliculas encontradas:')
    leer_vector(peliculas_x_genero)


def generar_matriz(): # (3)Determinar cantidad de peliculas Genero/Idioma.Mostrar mayores a 0.
    ma = [[0] * 6 for f in range(5)]
    return ma


def cargar_matriz(ma, vector):
    for i in range(len(vector)):
        ma[vector[i].idioma][vector[i].genero] += 1
    return ma


def lectura_matriz(ma):
    print("Las cantidad de peliculas por genero e idioma es:")
    print("|PELICULAS |INFANTIL|COMEDIA|ROMANTICO|DRAMA|CIENCIA FICCION|OTROS|")
    for f in range(len(ma)):
        print("|{:^10}|{:^8}|{:^7}|{:^9}|{:^5}|{:^15}|{:^5}|".format(IDIOMA[f],
                                                                     set_line(ma[f][0]), set_line(ma[f][1]),
                                                                     set_line(ma[f][2]), set_line(ma[f][3]),
                                                                     set_line(ma[f][4]), set_line(ma[f][5])))


def set_line(cantidad):
    if cantidad == 0:
        return "-"
    return cantidad


def consultar_cantidad(matriz): # (4)Determinar cantidad de peliculas del idioma (I).
    idioma = validar_int_entre(0, 4, "Ingrese el idioma de las peliculas que desea consultar cantidad:"
                                     "\n(0)Español\n(1)Inglés\n(2)Fracés\n(3)Portugués\n(4)Otros")
    print("-------------------------------------------------------------------------------------")
    cantidad = contador(matriz, idioma)
    print("La cantidad de peliculas en el idioma ", IDIOMA[idioma], "es de:", cantidad)


def contador(matriz, idioma):
    count = 0
    for genero in range(6):
        count += matriz[idioma][genero]
    return count


def busqueda_titulo(registro): # (5)Buscar en el vector la pelicula con el titulo (X).
    titulo = input("Ingrese el titulo de la pelicula que esta buscando: ")
    titulo = titulo.upper()
    indice = busqueda_binaria(registro, titulo)
    if indice >= 0:
        print(to_string_pelicula(registro[indice]))
    else:
        print("No se ha encontrado la pelicula solicitada.")
    return


def busqueda_binaria(registro, elemento):
    n = len(registro)
    izquierda = 0
    derecha = n - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if registro[medio].nombre == elemento:
            return medio
        elif registro[medio].nombre > elemento:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return -1


def seleccion_idioma(registros): # (6)Generar archivo de texto ,Idioma (X).
    idioma = validar_int_entre(0, 4, "Ingrese el idioma de las peliculas que desea guardar en el archivo:"
                                     "\n(0)Español\n(1)Inglés\n(2)Fracés\n(3)Portugués\n(4)Otros")
    registro_por_idioma(registros, idioma)
    return


def registro_por_idioma(registro, idioma):
    peliculas_en_el_idioma = []
    for i in range(len(registro)):
        if registro[i].idioma == idioma:
            insersion_ordenada(registro[i], peliculas_en_el_idioma)
    if not peliculas_en_el_idioma:
        print("No hay peliculas en ese idioma. Disculpe las molestias.")
        return
    else:
        archivo_por_idioma(peliculas_en_el_idioma, idioma)
    return
