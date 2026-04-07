# Ejercicio 2:
# ● Crear la clase Punto con dos atributos x e y (ambos numéricos), con el correspondiente
# constructor que recibe ambos valores.
# ● Definir métodos tales como:
# ○ eje_x
# ○ eje_y
# ○ impresion (método que devuelve en representación de string ambos valores)
# ○ opuesto (método que devuelve el punto o# negativosCualquierotromtodoquconsiderimpoclass Punto:
class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x
    
    def eje_y(self):
        return self.y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def opuesto(self):
        
        return Punto(-self.x, -self.y)

    def positivo_o_negativo(self):
        if self.x >= 0 and self.y >= 0:
            return "Ambos positivos"
        else:
            if self.x < 0 and self.y < 0:
                return "Ambos negativos"
            else:
                return "Uno positivo y otro negativo"
        
punto1 = Punto(3, 4)
punto2 = Punto(-3, -4)
print(punto1.__str__())
print(punto1.opuesto().__str__())   
print(punto1.positivo_o_negativo())
print(punto2.__str__())   
print(punto2.opuesto().__str__())
print(punto2.positivo_o_negativo())


# Ejercicio 3:
# Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que
# pasa la línea en un espacio de dos dimensiones.

# La clase dispondrá de los siguientes métodos:
# ● Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase
# Punto, que son utilizados para inicializar los atributos.
# ● mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
# ● mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
# ● mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
# ● mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique.
class Linea():
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b

    def mueve_derecha(self, distancia):
        self.punto_a.x += distancia
        self.punto_b.x += distancia
        
    def mueve_izquierda(self, distancia):
        self.punto_a.x -= distancia
        self.punto_b.x -= distancia
        
    def mueve_arriba(self, distancia):
        self.punto_a.y += distancia
        self.punto_b.y += distancia
        
    def mueve_abajo(self, distancia):
        self.punto_a.y -= distancia
        self.punto_b.y -= distancia

    def __str__(self):
        return f"Mi linea empieza en {self.punto_a} y termina en {self.punto_b}"
        
linea1 = Linea(Punto(1, 2), Punto(3, 4))
linea2 = Linea(Punto(5, 6), Punto(7, 8))

print(linea1.__str__())
print(linea2.__str__())
linea1.mueve_derecha(2)
linea1.mueve_arriba(3)
print(linea1.__str__())
linea1.mueve_izquierda(1)
linea1.mueve_abajo(1)   
print(linea1.__str__())


# Ejercicio 4:
# Desarrolla una clase Cancion con los siguientes atributos:
# ● titulo: una variable String que guarda el título de la canción.
# ● autor: una variable String que guarda el autor de la canción.
# Con los siguientes métodos:
# ● Cancion(String, String): constructor que recibe como parámetros el título y el autor de la
# canción (por este orden).
# ● get_titulo(): devuelve el título de la canción.
# ● get_autor(): devuelve el autor de la canción.
# ● set_titulo(String): establece el título de la canción.
# ● set_autor(String): establece el autor de la canción
class Cancion():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def set_titulo(self, titulo):
        self.titulo = titulo
        
    def set_autor(self, autor):
        self.autor = autor

cancion1 = Cancion("DeBeDe", "Sumo")
cancion2 = Cancion("La rubia tarada", "Sumo")
cancion3 = Cancion("Mañana en el Abasto", "Sumo")
print(cancion1.get_titulo() + " - " + cancion1.get_autor())
print(cancion2.get_titulo() + " - " + cancion2.get_autor())
print(cancion3.get_titulo() + " - " + cancion3.get_autor())


# Ejercicio 5:
# ● Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre
# cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar
# (ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes
# servicios: getters y setters, método para leer la información y método para mostrar la
# información.
# ● Este último método mostrará la información del libro con este formato:

# Título: Introduction to Java Programming 3a. edición
# Autor: Liang, Y. Daniel
# ISBN: 0-13-031997-X
# Prentice-Hall, New Jersey (USA)
# viernes 16 de noviembre de 2001
# 784 páginas

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre= nombre
        self.apellido = apellido
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Libro():
    def __init__(self, titulo, autor, isbm, paginas, edicion, editorial, lugar, fecha_edicion):
        self.titulo = titulo
        self.autor = autor
        self.isbm = isbm
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion

    def setter(self, titulo, autor, isbm, paginas, edicion, editorial, lugar, fecha_edicion):
        self.titulo = titulo
        self.autor = autor
        self.isbm = isbm
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion

    def getter(self):
        return self.titulo, self.autor, self.isbm, self.paginas, self.edicion, self.editorial, self.lugar, self.fecha_edicion
    
    def leer_informacion(self):
        self.titulo = input("Ingrese el título del libro: ")
        self.autor = input("Ingrese el autor del libro: ")
        self.isbm = input("Ingrese el ISBN del libro: ")
        self.paginas = int(input("Ingrese la cantidad de páginas del libro: "))
        self.edicion = input("Ingrese la edición del libro: ")
        self.editorial = input("Ingrese la editorial del libro: ")
        self.lugar = input("Ingrese el lugar de publicación del libro (ciudad y país): ")
        self.fecha_edicion = input("Ingrese la fecha de edición del libro (como texto): ")

    def mostrar_informacion(self):
        return f"Título: {self.titulo} ({self.edicion} edición)\nAutor: {self.autor}\nISBN: {self.isbm}\nEditorial: {self.editorial}, {self.lugar}\nFecha de edición: {self.fecha_edicion}\nCantidad de páginas: {self.paginas}"
    
libro1 = Libro("", "", "", 0, "", "", "", "")
libro1.leer_informacion()
print(libro1.mostrar_informacion())

#PD: Me ayudo un autocompletar del VS que no supe desctivar despues de que puse fix en un problema que vimos en clase cuando le comparti pantalla, aun asi, creo haber
#podido entender de manera correcta los principios de como se crea un objeto con la clase y se le dan o llaman datos con los metodos.


