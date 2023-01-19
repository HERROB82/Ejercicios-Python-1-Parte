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
# Lo que pongamos dentro del DEL es lo que queremos que pase justo antes de la eliminación por lo que se suelen poner mensajes informativos

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
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo,self.lanzamiento,self.duracion)

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
delattr(p1,"nombre") #Eliminamos el atributo nombre pero nunca atributos de clase
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

# Comprobacion
print(type(p_alien.titulo))
print(type(p_alien.duracion))
print(type(p_alien.lanzamiento))
print(type(p_alien.director))'''

# Algo mas AVANZADO: Creando un catalogo de peliculas (LISTA DE OBJETOS) #### REPASAR

# Retomamos la pelicula original
'''class Pelicula():

  #Constructor de clase
  def __init__(self,titulo,duracion,lanzamiento):
    self.titulo = titulo
    self.duracion = duracion
    self.lanzamiento = lanzamiento
    print("Se ha creado la pelicula: ",self.titulo)

  def __str__(self):
    return "{} ({})".format(self.titulo,self.lanzamiento)

class Catalogo():

  peliculas = [] #Esta lista contendra objetos de la clase Pelicula
  #El valor por defecto del catalogo es peliculas = [] (xq todavia no hay ninguna peliculas y esta vacio)
  def __init__(self,peliculas=[]):
    self.peliculas = peliculas
    if (len(self.peliculas) == 0):
        print("Se ha creado el catalogo vacio")
    else:
        print("Se ha creado el catalogo con  las peliculas asignadas")
  
  # Toda la interaccion que hagamos con las variables de una clase (es decir; modificacion, lectura, lo que sea) con los 
  # atributos de una clase SIEMPRE DEBERIA SER A TRAVES DE UN METODO!!
  def agregar(self,p):#x eso tengo aqui el metodo agregar que recibe un parametro (p) que sera un objeto de la clase pelicula
    self.peliculas.append(p) #le hacemos un append a "peliculas" xa ir agregando 
    print("Se ha agregado al catalogo la pelicula: {}".format(p.titulo)) #VER ESTO!!!! SI SE PUEDE

  def mostrar(self):
    for p in self.peliculas:
      print(p) #Print toma por defecto str(p)

# Ahora creamos los objetos peliculas
p1 = Pelicula("El Padrino",175,1972)
p2 = Pelicula("Alien el octavo pasajero",200,1979)
listaPeliculas=[p1,p2] #creamos una variable de listaPeliculas para verlo mas claro
print(type(listaPeliculas))

c = Catalogo(listaPeliculas) #creamos el objeto catalogo con dos peliculas que tb tenemos creadas
  
c.mostrar() #esta itera sobre la lista de objetos que existe en "c"

# Con esto añadimos una nueva pelicula directamente
c.agregar(Pelicula("El Padrino: Parte 2",202,1974))

# Alternativa a la linea anterior -- ESTA ES MEJOR!!
p3 = Pelicula("El Padrino: Parte 3",202,1980)
c.agregar(p3) # "c" es el objeto del catagolo y le invoco el metodo "agregar" y le paso el objeto "p3"

for peli in c.peliculas:
  print(peli.lanzamiento) #aqui ya voy poniendo .lanzamiento o .lo que quiera xa ver solo otro dato

c2 = Catalogo()
c2.mostrar()

# Creamos todo junto
pM1=Pelicula("Matrix",175,1999)
pM2=Pelicula("Matrix Reload",175,2003)
pM3=Pelicula("Matrix Revolution",175,2005)
c3 = Catalogo ([pM1,pM2,pM3])
c3.mostrar()'''


## CLASE Nº 4 ##

# Este comienza diciendo que no es herencia y que el ejercicio 5 de esta unidad es lo mismo que el ejercicio de películas 
# que van dentro de un catálogo, un pedido se compone varios productos (que vamos a ir metiendo) o unos productos van dentro 
# de pedido.

# Lo que da juego es una lista de objetos y nos habíamos quedado en el método de c.mostrar() que lo que hace es preguntarle
# al objeto c, qué tal si me listas tu lista de películas?, ya que la visualización no es simple sino que hay que visualizar
# una lista y para verlo esta utilizando un bucle for:
  
## Clase Nº 5 ##
# ENCAPSULACION #
# Consiste en denegar el acceso a los atributos y metodos internos de la clase desde el exterior
# En Python no existe, pero se puede simular precediendo atributos y metodos con dos barras bajas __:
# lo que dice la encapsulacion es que las variables no deberian salir nunca de una clase.
# En Python se crean variables privadas con dos guiones bajo x delante __atributo y esto siginidfica que solamente puede
# ser invocada desde su clase, por lo que no se puede llamar desde el MAIN

class Ejemplo():

  __atributo_privado = "Soy un atributo inalcanzable desde fuera"

  def __metodo_privado(self):
    print("Soy un metodo inalcanzable desde fuera")

# Programa principal (fuera de la clase Ejemplo)
e = Ejemplo()
e.__atributo_privado #Saldra por pantalla "Error de Atributo" ya que no puede llegar a el,ahi esta la encapsulacion
# el efecto practico es que estamos añadiendo una pequeña capa de seguridad, es lo mas basico de la seguridad

# No es lo mismo acceder a una variable que a un metodo; acceder a una variable es acceder al contenido por ende a los datos.
# Acceder a un metodo solo nos devuelve la posicion de memoria donde esta almacenado ese metodo, o sea que nada.

## ENCAPSULACION ##

#Getter: “Acceder Info”
#Setter: “Modificar Info”
#Solo puede haber 1 GET o 1 SET x cada Variable
#Cuando creamos una clase lo primero que tenemos que hacer es el :
#__INIT__
Variables (definimos las variables)
STR
GETTER y SETTER

# de todas las variables que hemos definidos hacemos un Getter y un Setter de c/u, y con eso tenemos pleno acceso pero de forma
# encapsulada a nuestra Clase) si queremos acceder al nombre invocamos al “get del nombre”, 
# si queremos cambiar el apellido invocamos al setter del apellido
# De esta manera desde donde sea vamos a ejecutar siempre métodos, creamos con el INIT, ver info STR, conseguir info con el GET
# y modificar algo será con el SET.


class Ejemplo():
  __atributo_privado = "Soy un metodo inalcanzable desde fuera"

  def __metodo_privado(self):
    print("Soy un metodo inalcanzable desde fuera")

  def metodo_publico(self):
    return self.__metodo_privado()
  # Getters
  @property
  def atributo_privado(self):
    print("Estoy en el GETTER")
    return self.__atributo_privado

  # Setter
  @atributo_privado.setter
  def atributo_privado(self,nuevoValor):
    print("Estoy en el SETTER")
    self.__atributo_privado = nuevoValor

  e = Ejemplo()







  











