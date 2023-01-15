# Ahora estamos viendo como pasar parámetros -> una es por posición(primera a primera posición, segunda a segunda posición, etc.) 
# pero también lo tenemos por nombre, ya que referenciando por nombre no queda ninguna duda sabor ej.:
# G3 = Galleta(sabor=”turrón”, chocolate = True)
# Por lo que las únicas formas que tenemos para enviar parámetros por posición son con a forma anterior, que es por NOMBRE'''

'''class Galleta():
  empresa = "Cuetara"

  def __init__(self, sabor, forma, chocolate):
    self.sabor = sabor
    self.forma = forma
    self.chocolate = chocolate

  def chocolatear(self):
    self.chocolate = True

  def tiene_chocolate(self):
    if self.chocolate:
      print("Soy una galleta chocolateada :)")
    else:
      print("Soy una galleta sin chocolate:(")


g = Galleta("salada", "cuadrada", True)
print(g.sabor)
print(g.forma)
print(g.chocolate)'''

# Valores por defectos en el constructor
# Y lo que esta diciendo ahora el profesor es que dejemos unos valores por defecto en el constructor, por eso ahora está poniendo sabor = None
# Por lo que si nosotros definimos a todas nuestras variables con un NONE por defecto (podemos poner cualquier otra cosa que NONE siempre y 
# cuando podamos controlar),la cosa es evaluar lo que hayamos puesto ahí, entonces cada vez que creemos objetos y 
# con los if podremos comprobar si sabor=! None and forma=!None

'''class Galleta():
  empresa = "Cuetara"

  def __init__(self, sabor=None , forma=None, chocolate=None):
    self.sabor = sabor
    self.forma = forma
    self.chocolate = chocolate
    if self.chocolate is not None and self.forma is not None and self.chocolate is not None:
      print("Se acaba de crear una galleta {}, {} y {}".format(self.sabor,self.forma,self.chocolate))
    else:
      print("Se acaba de crear una galleta pero...")
      if self.sabor is None:
        print(">El sabor no se ha definido")
      if self.forma is None:
        print(">La forma no se ha definido")
      if self.chocolate is None:
        print("> El chocolate no se ha definido")

    def chocolatear(self):
      self.chocolate = True

    def tiene_chocolate(self):
      if self.tiene_chocolate:
        print("Soy una galleta chocolateada :)")
      else:
        print("Soy una galleta sin chocolate:(")

# gracias a los valore spor defectos ninguna de los 4 objetos me ha dado error porqu no me para el programa
# en el momento que dudemos de que cuando creemos alguna galleta y no sepamos ningun valor de sabor forma o chocolate si creamos los valores
# por defecto si o si!!!

g = Galleta("salada", "cuadrada", True)
print(g.sabor)
print(g.forma)
print(g.chocolate)  

g2= Galleta("salada","cuadrada")
print(g2.sabor)
print(g2.forma)
print(g2.chocolate) 

g3=Galleta("salada")
print(g3.sabor)
print(g3.forma)
print(g3.chocolate)     

g4=Galleta() # aunque no tenga ningun parametro este objeto ha sido creado y luego pasa por el constructor y se define, coge las variables que les llegan, las mete dentro de sus atributos.
print(g4.sabor)
print(g4.forma)
print(g4.chocolate)'''


# METODOS ESPECIALES DE CLASE -- CONSTRUCTOR Y DESTRUCTOR

#Constructor de clase (al crearl a instancia)

'''class Pelicula():

    def __init__ (self,titulo=None,duracion=None,lanzamiento=None):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula",self.titulo)

p = Pelicula(180,1990)
print(p)'''

#Destructor de clase (al borrar la instancia)

#Creamos y eliminamos un objeto. OJO. Si reinstanciamos la misma variable mas de una vez, se crea de nuevo y se borra la anterior.
# Lo contrario a los constructores à DESTRUCTORES no lo destruye sino lo que hace es acabar de definirlo
# Xa borrar objetos lo que hacemos es liberar espacios, pero hoy en día es un proceso obsoleto.
# Lo que pongaos dentro del DEL es lo que queremos que pase justo antes de la eliminación por lo que se suelen poner mensajes informativos

'''class Pelicula():
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula",self.titulo)

    def __del__(self):
        print("Se ha borrado la pelicula",self.titulo)

p=Pelicula("El padrino",170,1972)
print(p)

del p #tambien admite varios parametros tipo del p,p2,p3
print(p) #cuando ejecute esto me saldra error de que name "p" no esta definido xq lo acabamos de borrar'''

# Mostrar informacion de un objeto : __dict__ y __str__

# Diccionario (__dict__)
# Python nos ofrece una forma predeterminada de mostrar la informacion de un objeto

'''class Pelicula():

    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula",self.titulo)
p = Pelicula("El padrino",172,1972)

print(p.__dict__)#nos devuelvo esto en formato DICCIONARIO
# Esto nos permite saber si nos pasan un objeto sin saber los atributos nosotros lo podemos sacar de esta manera.
# La forma directa de ver el contenido de un objeto es transformandolo a DICCIONARIO, asi vemos todos los atributos y todos los valores que tiene.

peli = p.__dict__ # podeos guardarla en una variable y almacenarla
print(peli)
print(type(peli))
print(peli["lanzamiento"]) #puedo acceder a valores de clave'''
# Accedemos a informacion de dentro de un objeto al transformarlo a diccionario MAYOR TRUCO DE PYTHON CON LA POO

#Clase 3.2 y el objetivo de hoy es poder imprimir la informacion de un objeto, ya que la informacion es encapsulada

'''class Pelicula():
    #Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula",self.titulo)

    #Destructor de clase
    #def __del__(self):
        #print("Se ha borrado la pelicula",self.titulo)

    #Redefinimos el metodo string
    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo,self.duracion,self.lanzamiento)

p1 = Pelicula("El Padrino",175,1072)
print(p1)#al hacer print del objeto, se esta invocando al metodo __str__ de nuestra clase
p = Pelicula("El padrino",172,1972)'''

# BONUS: Comprobar si un objeto pertenece a una clase

'''class Producto():
    pass

class Pedido():
    pass

class Cliente():
    pass

p1=Producto()
pd1=Pedido()
c1=Cliente()

print(isinstance(p1,Producto)) #dentro del parentesis tenemos que poner 2 cosas; el objeto que yo quiero evaluar y lo segundo el nombre de la clase
print(isinstance(c1,Producto))
print(isinstance(c1,(Producto,Pedido,Cliente))) #Tb se puede evaluar en una tupla todo lo que quiero evaluar.

# Bonus 2: Comprobar si un atributo existe dentro de una clase
# comprobamos que las variables precio y nombre si existen como atributos en el p1
# (aunque sean atributos distintos, uno es de instancia y otra de clase)

#es muy util de usar cuando tenemos objetos muy dispares entre si cuando no estamos seguros que todos los objetos sean homogeneos
print(hasattr(p1,"precio"))
print(hasattr(p1,"nombre"))
print(hasattr(p1,"apellidos"))
# comprobar si las variables y el precio y nombre son variables de clase en la clase Producto, si son atributos globales
print(hasattr(Producto,"precio")) #ponemos la clase ya que le estamos preguntando a ella directamente
print(hasattr(Producto,"nombre"))

# BONUS 3: Eliminar atributos de una instancia de clase

print(p1.__dict__) #Mostramos el objeto p1
#delattr(p1,"nombre") #Eliminamos el atributo nombre pero nunca atributos de clase
print(p1.__dict__) #Mostramos el objeto p1'''
# OJO con esto ya que todo lo que nos genere tene robjetos con estrucuturas diferentes eso nos va a complicar todo mucho mas cualquier 
# tipo de automatixacion que queramos hacer


# CLASE 3 ---> OBJETOS DENTRO DE OBJETOS <-------
# Recuperamos la clase Pelicula con la que ya hemos trabajado

'''class Pelicula():
    #Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento,director):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        self.director = director
        print("Se ha creado una pelicula",self.titulo)

    def __str__(self):
        return "{} ({}) --> {}".format(self.titulo,self.lanzamiento,self.director)

p1 = Pelicula("Matrix",120,1999,"Spielberg")

# Vamos a crear un director de cine:

class Director():
    # Constructor de clase
    def __init__(self,nombre,apellido,edad="desconocida"):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        print("Se ha creado el director {} {} con una edad {}".format(self.nombre,self.apellido,self.edad))

    def __str__(self):
        return "Director {} {} con edad {}".format(self.nombre,self.apellido,self.edad)

d1 = Director ("Ridley","Scott",84)
d2 = Director ("George","Lucas")  # pero cual es la diferencia entre objetos dentro de objeto a herencia? No hay relacion jerarquica

p_alien = Pelicula("Alien el octavo pasajero",200,1979,d1)
print(p_alien)
print(p_alien.director)#muestra el str de director
print(p_alien.director.nombre)#con esto solo podemos sacar el valor de nombre del objeto poniendo .nombre
print(p_alien.director.edad)

# Comprobacio
print(type(p_alien.titulo))
print(type(p_alien.duracion))
print(type(p_alien.lanzamiento))
print(type(p_alien.director))'''

# Algo mas AVANZADO: Creando un catalogo de peliculas (LISTA DE OBJETOS)

# Retomamos la pelicula original
class Pelicula():

  #Constructor de clase
  def __init__(self,titulo,duracion,lanzamiento):
    self.titulo = titulo
    self.duracion = duracion
    self.lanzamiento = lanzamiento
    print("Se ha creado la pelicula",self.titulo)

  def __str__(self):
    return "{} ({})".format(self.titulo,self.lanzamiento)

class Catalogo():

  peliculas = [] #Esta lista contendra objetos de la clase Pelicula
  #El valor por defecto del catalogo es peliculas = [] (xq todavia no hay ninguna peliculas y esta vacio)
  def __init__(self,peliculas[]):
    self.peliculas = peliculas
    if (len(peliculas == 0)):
      print("Se ha creado el catalogo vacio")
    else:
      print("Se ha creado el catalogo con  las peliculas asignadas")
  
  # Toda la interaccion que hagamos conlas variables de una clase (es decir; modificacion, lectura, lo que sea) con los 
  # atributos de una clase SIEMPRE DEBERIA SER A TRAVES DE UN METODO!!
  def agregar(self,p):#x eso tengo aqui el metodo agregar que recibe un parametro (p) que sera un objeto de la clase pelicula
    self.peliculas.append(p) #le hacemos un append a "peliculas" xa ir agregando 
    print("Se ha agregado al catalogo la pelicula: {}".format(p.titulo)) #VER ESTO!!!!

  











