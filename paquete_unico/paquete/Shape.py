import math

class ZeroSlopeError(Exception):
  def __init__(self, message):
    super().__init__(message)

class Point:
    definition: str = "Entidad geométrica abstracta que representa una ubicación en un espacio."
    
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x: float):
        self.__x = x

    def set_y(self, y: float):
        self.__y = y

    def move(self, new_x: float, new_y: float) -> None:
        self.set_x(new_x)
        self.set_y(new_y)

    def reset(self) -> None:
        self.__x = 0
        self.__y = 0

    def compute_distance(self, point: "Point") -> float:
        distance = ((self.__x - point.get_x()) ** 2 + (self.__y - point.get_y()) ** 2) ** 0.5
        return distance

class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.__start = start
        self.__end = end
        self.__length = self.compute_length()
        self.__slope = self.compute_slope()

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def get_length(self):
        return self.__length

    def get_slope(self):
        return self.__slope

    def set_start(self, start: Point):
        self.__start = start
        self.__length = self.compute_length()

    def set_end(self, end: Point):
        self.__end = end
        self.__length = self.compute_length()

    def compute_length(self) -> float:
        return self.__start.compute_distance(self.__end)

    def compute_slope(self) -> float:
        while True: # Ciclo para manejar la excepción de división por cero
            try: # Intentar calcular la pendiente
                slope = self.__slope = (self.__end.get_y() - self.__start.get_y()) / (self.__end.get_x() - self.__start.get_x())
                break
            except ZeroDivisionError: # Si x2 - x1 es cero, se aplica la excepción
                slope = float("inf") # Se guarda la pendiente como infinito
                break 
        return slope # Retorna la pendiente calculada

    def compute_horizontal_cross(self) -> float:
        if self.__slope == float("inf"):
            return float("inf") # Línea vertical
        Horicross = self.__start.get_y() - (self.__slope * self.__start.get_x())
        return Horicross


    def compute_vertical_cross(self) -> float:
        try: # Intenta calcular el corte vertical
            Vertcross =self.__start.get_x() - (self.__start.get_y() / self.__slope)
            return Vertcross
        except ZeroDivisionError:
            return float("inf") # Línea vertical

    def __str__(self) -> str: # Imprime la información de la línea
        slope_str = "Infinita" if self.__slope == float("inf") else f"{self.__slope:.2f}"
        string = f"""
        Línea desde ({self.__start.get_x()}, {self.__start.get_y()}) hasta ({self.__end.get_x()}, {self.__end.get_y()})
        Longitud: {self.__length:.2f}
        Pendiente: {slope_str}
        Corte horizontal (eje y): {self.compute_horizontal_cross():.2f}
        Corte vertical (eje x): {self.compute_vertical_cross():.2f}
        """
        return string

class Shape:
    def __init__(self):
        self.__is_regular = False

    def get_is_regular(self):
        return self.__is_regular

    def set_is_regular(self, is_regular: bool):
        self.__is_regular = is_regular

    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar compute_area()")

    def compute_perimeter(self):
        raise NotImplementedError("Subclases deben implementar compute_perimeter()")

class Triangle(Shape):
    
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__()
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
        self.__update_sides()


    def get_points(self):
        return (self.__p1, self.__p2, self.__p3)

    def set_points(self, p1: Point, p2: Point, p3: Point):
        self.__p1, self.__p2, self.__p3 = p1, p2, p3
        self.__update_sides()

    def get_sides(self):
        return (self.__a, self.__b, self.__c)

    def __update_sides(self):
        self.__a = self.__p2.compute_distance(self.__p3)
        self.__b = self.__p1.compute_distance(self.__p3)
        self.__c = self.__p1.compute_distance(self.__p2)

    def compute_perimeter(self):
        return self.__a + self.__b + self.__c

    def compute_area(self):
        s = self.compute_perimeter() / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def compute_inner_angles(self): # Para todos los triángulos
        try: # Se intenta calcular los ángulos usando la ley de cosenos
            A = math.degrees(math.acos((self.__b**2 + self.__c**2 - self.__a**2) / (2 * self.__b * self.__c)))
            B = math.degrees(math.acos((self.__a**2 + self.__c**2 - self.__b**2) / (2 * self.__a * self.__c)))
            C = math.degrees(math.acos((self.__a**2 + self.__b**2 - self.__c**2) / (2 * self.__a * self.__b)))  
            return (A, B, C)
        except ValueError: # Pero con C se genera un error al obtener un valor fuera del rango {-1, 1}
            C = 180 - (A + B) # Entonces se calcula C como el complemento de A y B
            return (A, B, C)

    def __str__(self): # Imprime la información del triángulo
        string = f"""
            Triángulo con vértices "
            A({self.__p1.get_x()}, {self.__p1.get_y()}),
            B({self.__p2.get_x()}, {self.__p2.get_y()}),
            C({self.__p3.get_x()}, {self.__p3.get_y()})"
            , lados: a={self.__a:.2f}, b={self.__b:.2f}, c={self.__c:.2f}"
            , área: {self.compute_area():.2f}, perímetro: {self.compute_perimeter():.2f}"
            , ángulos internos: {self.compute_inner_angles()}"
        """
        return string

class Scalene(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)

    def __str__(self):
        return f"Triángulo Escaleno: {super().__str__()}"

class Isosceles(Triangle):
    def __init__(self, base: float, side: float, origin: Point = Point(0, 0)):
        p1 = origin
        p2 = Point(origin.get_x() + base, origin.get_y())
        altura = math.sqrt(side**2 - (base / 2)**2)
        p3 = Point(origin.get_x() + base / 2, origin.get_y() + altura)
        super().__init__(p1, p2, p3)

    def __str__(self):
        return f"Triángulo Isósceles: {super().__str__()}"

class Equilateral(Triangle):
    def __init__(self, side: float, origin: Point = Point(0, 0)):
        p1 = origin
        p2 = Point(origin.get_x() + side, origin.get_y())
        altura = math.sqrt(3) / 2 * side
        p3 = Point(origin.get_x() + side / 2, origin.get_y() + altura)
        super().__init__(p1, p2, p3)

    def compute_inner_angles(self):
        return (60.0, 60.0, 60.0)

    def compute_area(self):
        a, _, _ = self.get_sides()
        return (math.sqrt(3) / 4) * a**2

    def __str__(self):
        return f"Triángulo Equilátero: {super().__str__()}"

class TriRectangle(Triangle):
    def __init__(self, base: float, height: float, origin: Point = Point(0, 0)):
        p1 = origin
        p2 = Point(origin.get_x() + base, origin.get_y())
        p3 = Point(origin.get_x(), origin.get_y() + height)
        super().__init__(p1, p2, p3)

    def compute_area(self):
        a, b, c = self.get_sides()
        return (a * b) / 2

    def __str__(self):
        return f"Triángulo Rectángulo: {super().__str__()}"

class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__()
        method = kwargs.get("method", "1")
        if method == "1":
            corner: Point = kwargs.get("corner", Point())
            self.__width = kwargs.get("width", 1)
            self.__height = kwargs.get("height", 1)
            self.__center = Point((corner.get_x() + self.__width) / 2, (corner.get_y() + self.__height) / 2)
        elif method == "2":
            center: Point = kwargs.get("center", Point())
            self.__center = center
            self.__width = kwargs.get("width", 1)
            self.__height = kwargs.get("height", 1)
        elif method == "3":
            corner1: Point = kwargs.get("corner1", Point())
            corner2: Point = kwargs.get("corner2", Point())
            self.__width = abs(corner2.get_x() - corner1.get_x())
            self.__height = abs(corner2.get_y() - corner1.get_y())
            self.__center = Point((corner1.get_x() + corner2.get_x()) / 2, (corner1.get_y() + corner2.get_y()) / 2)
        else:
            lines: list = kwargs.get("lines", [])
            self.__width = lines[0].get_length()
            self.__height = lines[1].get_length()
            self.__center = Point(
                (lines[0].get_start().get_x() + lines[0].get_end().get_x()) / 2,
                (lines[0].get_start().get_y() + lines[1].get_end().get_y()) / 2
            )

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_center(self):
        return self.__center

    def set_width(self, width: float):
        self.__width = width

    def set_height(self, height: float):
        self.__height = height

    def set_center(self, center: Point):
        self.__center = center

    def compute_area(self) -> float:
        return self.__width * self.__height

    def compute_perimeter(self) -> float:
        return 2 * (self.__width + self.__height)

    def compute_interference_point(self, point: Point) -> bool:
        left = self.__center.get_x() - self.__width / 2
        right = self.__center.get_x() + self.__width / 2
        bottom = self.__center.get_y() - self.__height / 2
        top = self.__center.get_y() + self.__height / 2
        if left <= point.get_x() <= right and bottom <= point.get_y() <= top:
            print(f"El punto ({point.get_x()}, {point.get_y()}) está dentro del rectángulo.")
            return True
        else:
            print(f"El punto ({point.get_x()}, {point.get_y()}) está fuera del rectángulo.")
            return False

    def compute_interference_line(self, line: "Line") -> None:
        if self.compute_interference_point(line.get_start()) and self.compute_interference_point(line.get_end()):
            print("La línea está completamente dentro del rectángulo.")
        elif self.compute_interference_point(line.get_start()) or self.compute_interference_point(line.get_end()):
            print("La línea intersecta el rectángulo.")
        else:
            print("La línea está completamente fuera del rectángulo.")

    def __str__(self) -> str: # Imprime la información del rectángulo
        string = f"""
        Rectángulo centrado en ({self.__center.get_x()}, {self.__center.get_y()}) con ancho {self.__width} y alto {self.__height}.
        Área: {self.compute_area()}
        Perímetro: {self.compute_perimeter()}
        """
        return string


class Square(Rectangle):
    def __init__(self, side: float = 1, center: Point | None = None):
        if center is None:
            center = Point()
        super().__init__(method="2", width=side, height=side, center=center)

    def __str__(self) -> str:
        string = f"""
        Cuadrado centrado en ({self.get_center().get_x()}, {self.get_center().get_y()}) con lado {self.get_width()}.
        Área: {self.compute_area():.2f}
        Perímetro: {self.compute_perimeter():.2f}
        """
        return string