class TipoInvalidoException(Exception):
  def __init__(self, message):
    super().__init__(message)

def Mismos_Caracteres():
    # Declaración de variables
    dicc_conjuntos : dict = {}
    lis_lis_palabras : list = []
    palabra_lista : list = []
    lista_palabras : list = []
    lista_parejas : list = []

    print("Ingresa palabras para comparar si tienen los mismos caracteres")
    print("(Presiona Enter para finalizar)\n")
    while True: # Ciclo para ingresar palabras
        palabra_lista = []
        palabra = str(input("Ingresa una palabra: \n"))
        if palabra == "":
            break
        elif not palabra.isalpha():  # Si el dato ingresado no es una palabra llama al error
            raise TipoInvalidoException("Error: Entrada inválida. Por favor ingresa una palabra")
        palabra = palabra.lower() # Se convierte a minúsculas para evitar errores por mayúsculas
        for i in palabra:
            palabra_lista.append(i) # Se crea una lista con los caracteres de la palabra
        lista_palabras.append(palabra) # Se crea una lista con las palabras ingresadas
        lis_lis_palabras.append(palabra_lista) # Se crea una lista de listas con los caracteres de cada palabra
    
    # Creación del diccionario con las palabras que tienen los mismos caracteres
    for i in range(len(lis_lis_palabras)):
        for j in range(len(lis_lis_palabras)):
            if lis_lis_palabras[i] == lis_lis_palabras[j]:
                continue # Se omite la misma palabra
            else: # Se comparan las palabras por sus caracteres ordenados
                if (sorted(lis_lis_palabras[i])) == (sorted(lis_lis_palabras[j])):
                    lista_parejas.append((lista_palabras[j])) # Se agrega la palabra a la lista de parejas
        dicc_conjuntos[lista_palabras[i]] = lista_parejas # Se agrega la lista de parejas por palabra al diccionario
        lista_parejas = [] # Se reinicia la lista de parejas para la siguiente palabra

    # Mostrar resultados
    print("Para cada palabra, estas son las que tienen los mismos caracteres:")
    for clave in dicc_conjuntos: # Se itera por las claves del diccionario
        print(f"{clave} : {dicc_conjuntos[clave]}") # Imprimiendo la palabra y su lista de parejas


if __name__ == '__main__': # Función main para iniciar el código
    Mismos_Caracteres()