# Reto 6 POO
Para el reto # 6 se pedían dos cosas, primero añadir excepciones a los programas diseñados en el reto # 1, y segundo, identificar o corregir 3 casos en donde fuesen necesarias las excepciones en el paquete "Shape", que se ha venido trabajando en distintos retos.
***
## Logo del grupo
![Logo](https://github.com/NotName-K/POO-R2/blob/main/Screenshot%202025-09-23%20110719.png?raw=true)
## Excepciones que fueron utilizadas
***
### División por Cero
```python
class DivisionPorCeroException(Exception):
  def __init__(self, message):
    super().__init__(message)
```
### Tipo inválido
```python
class TipoInvalidoException(Exception):
  def __init__(self, message):
    super().__init__(message)
```
Y por supuesto, el infaltable **ValueError**.
## Exepciones en el reto #1
***
### Operador de números
Este programa recibe 2 valores enteros y el usuario elige la operación que se les realizará, mostrando en consola al final el resultado, para esto lógicamente el usuario debe ingresar estos valores, y si no son enteros se generará un "ValueError", lo que se reportará al usuario y se repetirá el bucle hasta que ambos valores sean válidos.
```python
    while True: # Ciclo para ingresar los valores correctamente
        try:
            a = int(input("Digita el primer valor:"))
            b = int(input("Digita el segundo valor:"))
            break
        except ValueError: # Si no son números enteros, se lanza el error
            print("Error: Entrada inválida. Por favor ingresa un número entero")
```
Por otro lado, si el segundo valor es cero, y se escoge la opción 4, se realizaría una división por cero, sin embargo, se le especifica al programa que solo debe realizarla si b es diferente a cero, sino, llamará al error "DivisionPorCero", y se le reportará al usuario.
```python
elif operacion == 4:
   if b != 0: # Si b no es cero, se realiza la división
      num = a / b
   else: # Se llama al error de división por cero y se termina el programa
      raise DivisionPorCeroException("Error: No se puede dividir entre cero.")
```
### Verificador de Palíndromo
En este programa se le pide al usuario una palabra la cual se desglozará en letras y se invertirá para verificar si es o no palíndroma, pero, para esto se necesita que el string ingresado si sea una palabra, así que si python recibe algo que no son letras (not Palabra.isalpha), llama al error y se termina el programa.
```python
    while True: # Ciclo para ingresar la palabra
       Palabra = str(input("Ingrese una palabra para verificar si es un palíndromo:"))
       if not Palabra.isalpha():  # Si el dato ingresado no es una palabra llama al error
           raise TipoInvalidoException("Error: Entrada inválida. Por favor ingresa una palabra")
       break
```
### Lista de números primos
En este programa el usuario ingresa una lista de números enteros los cuáles posteriormente son divididos hasta el número siguiente a su mitad y si alguno de sus módulos es 0, no se considerará primo, en caso contrario se ingresa a una lista donde se guardan los que sí. El único error posible es al momento de ingresar los valores, de tal forma que se utiliza un ValueError para, en caso de que se de, cerrar el bucle de ingreso de datos.
### Mayor suma en cercanía
En este programa se ingresa una lista de números y se realizan las sumas de dichos números con aquellos que se ingresaron antes y después, de tal forma que luego se guardan en una lista que se organiza ascendentemente, y se escoge el último valor, que representa la mayor suma en las cercanías. Del mismo modo que el caso anterior, se utiliza el ValueError para cerrar el bucle de ingreso de datos.
```python
    while True: # Ciclo infinito, se rompe con el break
        try:
            lista_numeros.append(int(input("Ingresa un número: \n")))
        except ValueError: # Cuando se ingresa un valor no numérico, se rompe el ciclo
            break
```
### Palabras con iguales caracteres
Este programa crea una lista con palabras ingresadas, las cuales divide en sus caracteres y verifica palabra por palabra, si al ordernarlos alfabéticamente, son iguales, en cuyo caso, se agrega la palabra comparada a una lista de parejas de la correspondiente palabra con la que se comparó, imprimiendo dichas parejas al final. El error se da cuando se ingresan los string, ya que se necesita que no tengan nada diferente a letras, por lo que en caso de que sí lo tengan, se llama al error de Tipo inválido.
```python
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
```
## Exepciones en el paquete Shape
***
### Cálculo de pendientes
En el caso de las Líneas, una de sus propiedades es la pendiente, que indica una relación entre sus coordenadas en "X" y en "Y", esta se calcula con una división de las posiciones finales menos las posiciones iniciales, en el numerador va el eje y, y en el denominador el x, si ambas coordenadas en x son iguales, su resta es igual y cero y se daría una división por cero, así que el programa al notar esto, con el except evita que termine el programa y guarda la pendiente como "infinita".
```python
    def compute_slope(self) -> float:
        while True: # Ciclo para manejar la excepción de división por cero
            try: # Intentar calcular la pendiente
                slope = self.__slope = (self.__end.get_y() - self.__start.get_y()) / (self.__end.get_x() - self.__start.get_x())
                break
            except ZeroDivisionError: # Si x2 - x1 es cero, se aplica la excepción
                slope = float("inf") # Se guarda la pendiente como infinito
                break 
        return slope # Retorna la pendiente calculada
```
### Cálculo de ángulos internos
En el caso de los triángulos, todos estos tienen ángulos internos que al sumarlos da 180 grados, para hallarlos de forma general sin importar el tipo de triángulo, se utiliza la ley de cosenos, sin embargo depende de la función "Arco Coseno" que funciona en el intervalo [-1,1], sin embargo python al hacer el cálculo puede salirse un poco de este, por lo que en caso de que se de un Value Error, se calculará C como el complemento de A y B, es decir restando 180 menos los ángulos ya mencionados.
```python
    def compute_inner_angles(self): # Para todos los triángulos
        try: # Se intenta calcular los ángulos usando la ley de cosenos
            A = math.degrees(math.acos((self.__b**2 + self.__c**2 - self.__a**2) / (2 * self.__b * self.__c)))
            B = math.degrees(math.acos((self.__a**2 + self.__c**2 - self.__b**2) / (2 * self.__a * self.__c)))
            C = math.degrees(math.acos((self.__a**2 + self.__b**2 - self.__c**2) / (2 * self.__a * self.__b)))  
            return (A, B, C)
        except ValueError: # Pero con C se genera un error al obtener un valor fuera del rango {-1, 1}
            C = 180 - (A + B) # Entonces se calcula C como el complemento de A y B
            return (A, B, C)
```
### Cálculo del cruce de una línea con el eje vertical
De vuelta a las líneas, se verifica el cruce de estas con los ejes, específicamente para el vertical se utiliza la siguiente fórmula, sin embargo, en esta se divide por la pendiente, pero si la pendiente es zero, se generaría un error, con lo que se agrega una estructura Try-Except, en donde al darse este error se retorna el cruce como infinito y se evita terminar el programa.
```python
    def compute_vertical_cross(self) -> float:
        try: # Intenta calcular el corte vertical
            Vertcross =self.__start.get_x() - (self.__start.get_y() / self.__slope)
            return Vertcross
        except ZeroDivisionError:
            return float("inf") # Línea vertical
```
