def mayor_suma(): # función requerida
    
    # Declaración e inicialización de variables
    lista_numeros : list = [] 
    lista_sumas : list = [] 
    suma: float = 0 
    valor_viejo: float = 0

    # Se pide la lista de números al usuario
    print("Ingresa números enteros para determinar la mayor suma posible")
    print("(Presiona Enter para finalizar)\n")
    while True: # Ciclo infinito, se rompe con el break
        try:
            lista_numeros.append(float(input("Ingresa un número: \n")))
        except ValueError: # Fin del ciclo al ingresar un valor no numérico
            break
    
    # Se calculan las sumas de números consecutivos y se almacenan en una lista    
    for num in range(1, len(lista_numeros)): 
        suma = lista_numeros[num-1] + lista_numeros[num]
        lista_sumas.append(suma)
        suma = 0
    
    # Se ordenan las sumas de menor a mayor
    for i in range(1, len(lista_sumas)):
        for j in range(0, len(lista_sumas)):
            if lista_sumas[i] < lista_sumas[j]:
                valor_viejo = lista_sumas[i]
                lista_sumas[i] = lista_sumas[j]
                lista_sumas[j] = valor_viejo
                valor_viejo = 0

    # Se muestra la mayor suma posible
    print(f"\nLa mayor suma posible es: {lista_sumas[-1]}")
    print(f"Estos fueron los resultados obtenidos: {lista_sumas}")
if __name__ == '__main__': # Función main para iniciar el código
    mayor_suma()