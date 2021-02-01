import os.path
import pickle


NOMBRES_PELICULAS = ["BUSCANDO A NEMO", "CIUDAD DE DIOS", "HABLE CON ELLA", "KANDAHAR", "LA MIRADA DE ULISES",
                     "CHUNKING EXPRESS", "PULP FICTION", "SCHINDLER", "PERSONA", "BANDE A PART", "TELEFONO ROJO",
                     "VOLAMOS HACIA MOSCU", "CUENTOS DE TOKIO", "MARGARITA GAUTIER", "HISTORIAS DE LA LUNA", "VIVIR",
                     "UMBERTO D", "PINOCHO", "NINOTCHKA", "OLIMPIA", "EL BAZAR", "LE CRIME", "DESENGAÑO",
                     "EN ALAS DE LA DANZA", "FRANKEINTEIN", "ITS A GIFT", "LUCES DE LA CIUDAD", "EL MUNDO EN MARCHA",
                     "EL ULTIMO EN ORDEN", "METROPOLIS", "INTERESTELAR"]
GENERO = ["INFANTIL", "COMEDIA", "ROMANTICO", "DRAMA", "CIENCIA FICCION", "OTROS"]
IDIOMA = ["ESPAÑOL", "INGLES", "FRANCES", "PORTUGUES", "OTROS"]
ARCHIVO = "Peliculas.dat"


class Pelicula:
    def __init__(self, nombre, genero, idioma):
        self.nombre = nombre
        self.genero = genero
        self.idioma = idioma


def insersion_ordenada(pelicula, vector):
    len_re = len(vector)
    izquierda = 0
    derecha = len_re - 1
    pos = len_re

    while derecha >= izquierda:
        cociente = (izquierda + derecha) // 2
        if vector[cociente].nombre == pelicula.nombre:
            pos = cociente
            break
        if vector[cociente].nombre > pelicula.nombre:
            derecha = cociente - 1
        else:
            izquierda = cociente + 1
    if izquierda > derecha:
        pos = izquierda

    vector[pos:pos] = [pelicula]
    return vector


def lectura_binario():  # Lectura del archivo para la creacion del arreglo
    manejador = open(ARCHIVO, "rb")
    arreglo = []
    size = os.path.getsize(ARCHIVO)

    while manejador.tell() < size:
        pelicula = pickle.load(manejador)
        insersion_ordenada(pelicula, arreglo)

    manejador.close()
    return arreglo


def leer_vector(vector):
    for i in vector:
        print(to_string_pelicula(i))


def archivo_por_idioma(registros, idioma):  # (6) Creacion del archivo correspondiente.
    name_file = "Peliculas_en_" + IDIOMA[idioma] + ".txt"
    archivo_abierto = open(name_file, "w")
    for i in range(len(registros)):
        string = to_string_pelicula(registros[i]) + "\n"
        archivo_abierto.write(string)
    archivo_abierto.close()
    print("¡El archivo ha sido creado con éxito!")


def to_string_pelicula(pelicula):
    string = "Pelicula: Nombre: {:<20} | Genero: {:<15} | Idioma: {:<12}".format(pelicula.nombre,
                                                                                 GENERO[pelicula.genero],
                                                                                 IDIOMA[pelicula.idioma])
    return string
