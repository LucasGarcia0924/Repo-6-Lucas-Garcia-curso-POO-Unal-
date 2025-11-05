def primos(): # función requerida
    # Declaración e inicialización de variables
    lista_numeros : list = [] 
    lista_primos : list = [] 
    
    # Se pide la lista de números al usuario
    print("Ingresa números enteros para determinar cuáles son primos (Presiona Enter para finalizar)\n")
    while True: # Ciclo infinito, se rompe con el break
        try:
            lista_numeros.append(int(input("Ingresa un número: \n")))
        except ValueError: # Cuando se ingresa un valor no numérico, se rompe el ciclo
            break

    # Se verifica cuáles números son primos
    for i in lista_numeros:
        if i < 2: # Los números menores a 2 no son primos
            continue
        elif i == 2: # El 2 es primo pero no cumple el próximo condicional
            lista_primos.append(i)
        else:
            # Si el número es divisible por otro entre 2 y su mitad, pasa al siguiente
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else: # Si no se encontró ningún divisor, se agrega a la lista de números primos
                lista_primos.append(i)
    
    # Se itera por los elementos de la lista de números primos para mostrarlos
    print("\nLos valores ingresados que hacen parte de los números primos son:\n")
    for num in lista_primos:
        print(f"{num}")
    
if __name__ == '__main__': # Función main para iniciar el código
    primos()