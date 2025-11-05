class DivisionPorCeroException(Exception):
  def __init__(self, message):
    super().__init__(message)

def operaciones(): # Función requerida
    # Declaración e inicialización de variables
    while True: # Ciclo para ingresar los valores correctamente
        try:
            a = int(input("Digita el primer valor:"))
            b = int(input("Digita el segundo valor:"))
            break
        except ValueError: # Si no son números enteros, se lanza el error
            print("Error: Entrada inválida. Por favor ingresa un número entero")
    num : float = 0
    bandera: bool = True
    print("Elige la operación a realizar:")
    
    while bandera == True:
        try: # Ciclo ideal, se rompe con el cambio en la bandera
            operacion =int(input("Sumar (1), Restar (2), Multiplicar (3) o Dividir (4)"))
            if operacion == 1:
                num = a + b
            elif operacion == 2:
                num = a - b
            elif operacion == 3:
                num = a * b
            elif operacion == 4:
                if b != 0: # Si b no es cero, se realiza la división
                    num = a / b
                else: # Se llama al error de división por cero y se termina el programa
                    raise DivisionPorCeroException("Error: No se puede dividir entre cero.")
            else:
                print("Elección no válida. Intenta de nuevo.")
                continue
            bandera = False
        except ValueError: # Caso de error por si se agrega un valor inválido
            print("Error: Entrada inválida. Por favor ingresa un número entero")
            continue
    # Se entrega el resultado final
    print(f"El resultado de la operación es: {num}")

if __name__ == '__main__': # Función main para iniciar el código
    operaciones()