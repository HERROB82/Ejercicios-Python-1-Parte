## EJEMPLO 1 DATOS DE CLIENTES ##

'''class Cliente():

    def __init__(self,dni,nombre,apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self): # devuelve una representacion de cadena del objeto 'Cliente'
        return "{} {}".format(self.nombre,self.apellidos)
    
class Empresa():

    def __init__(self,clientes=[]): # aqui el parametro CLIENTES es una lista de objetos
        self.clientes = clientes

    # aqui el metodo 'MOSTRAR_CLIENTE' toma un parametro 'DNI' y busca un objeto 'CLIENTE' en la lista de clientes de la empresa que tenga    
    # ese dni. Si lo encuentra, el metodo lo imprime utilizando el metodo 'STR'
    def mostrar_cliente(self,dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    # este metodo tb toma un parametro 'dni' y busca en la lista de clientes de la empresa un objeto 'CLIENTE' q tenga ese dni.
    # Si lo encuentra, elimina el objeto 'CLIENTE' de la lista y luego imprime el print.
    def borrar_cliente (self,dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"--> BORRADO")
                return
        print("Cliente no encontrado")

# Creamos un par de clientes

Hernan = Cliente(nombre="Hernan",apellidos="Salemme Zegianini",dni="0990988r7")
Juan = Cliente("2222228","Juan","Gonzalez Marquez")

# creamos una empresa con los clientes iniciales
empresa = Empresa(clientes=[Hernan,Juan])

# Mostramos todos los clientes
print("==LISTADO DE CLIENTES==")
print(empresa.clientes)

print("==MOSTRAR CLIENTES POR DNI==")
# consulto clientes por DNI
empresa.mostrar_cliente("0990988r7")
empresa.mostrar_cliente("2222228")

print("==BORRAR CLIENTES POR DNI==")
# borro un clientes por DNI
empresa.borrar_cliente("09908r7")
empresa.borrar_cliente("2222228")

# Mostramos todos los clientes
print("==LISTADO DE CLIENTES==")
print(empresa.clientes)'''

## EJEMPLO 2 GALLETAS ## (creando el primer constructor)

'''class Galleta():
    chocolate = False #atributo de clase

    def __init__(self):
        print("se acaba de crear una galleta")

    # este es un metodo de instancia que cambia el valor del atributo 'chocolate' de la galleta a "True"
    # el atributo 'chocolate' es un atributo de clase por lo que es compartido x todas las instancias de  la clase 'Galleta'
    def chocolatear(self):
        self.chocolate = True

    # es un metodo de instancia que comprueba el valor del atributo 'chocolate' de la galleta e imprime un mensaje en consola que indica
    # si la galleta tiene chocolate o no
    def tiene_chocolate(self):
        if self.chocolate:
            print("Soy una galleta chocolateada :-)")
        else:
            print("Soy una galleta sin chocolate :-()")

g =Galleta()
g.tiene_chocolate() # aqui como el valor del atributo 'chocolate' es FALSE de forma predeterminada, la galleta no tiene chocolate
g.chocolatear() # con este metodo cambiamos el valor del atributo 'chocolate' a TRUE x lo que ahora la galleta tendra chocolate
g.tiene_chocolate() # como el valor del atributo ha cambiado a TRUE saldra el mensaje de que si tiene chocolate
'''

## EJEMPLO 3 GALLETAS ## (Le pasamos parametros al Constructor)

'''class Galleta():

    def __init__ (self,sabor,forma):
        self.sabor = sabor
        self.forma = forma
        print("Se acaba de crear una galleta {} y {}".format(sabor,forma))

    # este metodo no esta implementado en la clase pero se puede agregar xa hacer que la galleta tenga chocolate
    def chocolatear(self):
        self.chocolate = True

    # verifica si la galleta tiene chocolate o no
    def tiene_chocolate(self):
        if self.chocolate:
            print("Soy una galleta chocolateada :-)")
        else:
            print("Soy una galleta sin chocolate :-()")

g = Galleta("salada","cuadrada")
g2= Galleta() # dara error xq faltan pasarle los argumentos'''

## EJEMPLO 4 GALLETAS ## (Le pasamos parametros al Constructor,pero ahora no los definimos y los ponemos todos con NONE)

'''class Galleta():
    chocolate = False

    def __init__(self,sabor = None,forma = None):
        self.sabor = sabor
        self.forma = forma
        if sabor is not None and forma is not None: # aqui si no se  proporcionan valores saldra  el mensaje de que no se puede crear galleta
            print("Se ha creado una galleta {} y {}".format(sabor,forma))
        else:
            print("No se puede crear la galleta sin sabor ni forma")

    def chocolatear(self):
        self.chocolate = True

    # verifica si la galleta tiene chocolate o no
    def tiene_chocolate(self):
        if self.chocolate:
            print("Soy una galleta chocolateada :-)")
        else:
            print("Soy una galleta sin chocolate :-()")

g = Galleta("salada","cuadrada")
g2 = Galleta()'''

## EJEMPLO 4 Peliculas y Metodo __DEL__ ## Borramos instancias con el metodo DEL

'''class Pelicula():
    # constructor de la clase
    def __init__ (self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("se ha creado la pelicula",self.titulo)

    #destructor de la clase
    def __del__(self):
        print("se ha borrado la pelicula",self.titulo)

p = Pelicula("El Padrino",175,1972)
del p'''


## EJEMPLO 5 Peliculas y Metodo __STR__ ##  xa devolver cadena de texto x defecto

'''class Pelicula():
    # constructor de la clase
    def __init__ (self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("se ha creado la pelicula",self.titulo)

    # destructor de la clase
    def __del__(self):
        print("se ha borrado la pelicula",self.titulo)

    # redefinimos el  metodo string q devuelve una cadena
    def __str__ (self):
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo,self.lanzamiento,self.duracion)
    
p1 = Pelicula("El Padrino",175,1972)
print(p1)'''


## EJEMPLO 6 Peliculas y Creacion de OBJETOS DENTRO de OBJETOS## listas + append + for

'''class Pelicula():
    # constructor de la clase
    def __init__ (self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("se ha creado la pelicula",self.titulo)

    def __str__(self):
        return "{} ({})".format(self.titulo,self.lanzamiento)
    
    # AHORA CREAMOS UN CATALAGO DE PELICULAS

class Catalogo():

    peliculas = []

    def __init__(self,peliculas=[]):
        self.peliculas = peliculas
        print("Se ha creado el catalogo")

    #este metodo aqrega peliculas a la lista de CATALOGO
    def agregar(self,p): # p sera un objeto de Pelicula
        self.peliculas.append(p)
        print("Se ha agregado al catalogo la pelicula: {}".format(p.titulo))

    def mostrar (self):
        for p in self.peliculas:
            print (p) #Print toma x defecto str(p)

p = Pelicula("El Padrino",175,1972)
c = Catalogo([p])

c.mostrar() # vemos el objeto peliculas que tengamos
c.agregar (Pelicula("El Padrino: Parte 2",202,1974)) # Añadimos una pelicula directamente
c.mostrar()

# ahora vamos a crear un catalogo vacio
c2 = Catalogo()
c2.mostrar()

# y ahora vamos a crear un catalogo con mas peliculas
pM1 = Pelicula("Matrix",175,1999)
pM2 = Pelicula("Matrix Reloaded",180,2002)
pM3 = Pelicula("Matrix Revolutions",190,2004)
c3 = Catalogo([pM1,pM2,pM3])
c3.mostrar()
'''

## EJEMPLO 7 ENCAPSULACION ## GETTERS Y SETTERS

'''class Ejemplo():
    __atributo_privado = "Soy un atributo inalcanzable desde fuera" # el uso del doble guion hace al atributo privado

    def __metodo_privado(self): #aqui definimos al metodo privado lo q hace q solo se puede acceder a el desde dentro de la clase
        print("Soy un atributo inalcanzable desde fuera")

    def metodo_publico(self):
        return self.__metodo_privado()
    #GETTER
    @property
    def atributo_privado(self):
        print("ESTOY EN EL GETTER")
        return self.__atributo_privado
    
    #SETTER
    @atributo_privado.setter
    def atributo_privado(self,nuevoValor):
        print("ESTOY EN EL SETTER")
        self.__atributo_privado = nuevoValor

# Programa principal (fuera de la clase Ejemplo)
e= Ejemplo()

# probamos a acceder a un atributo y observamos que se hace a traves del GETTER
print(e.atributo_privado)

# probamos a modificar un atributo y observamos que se hace a traves del SETTER
e.atributo_privado = "hola mundo"
print(e.atributo_privado)

# x ultimo comprobamos que podemos acceder al metodo privado a traves del metodo publico
e.metodo_publico()
'''

## EJEMPLO 8 ENCAPSULACION ## GETTERS Y SETTERS CON DIFERENTE NOMBRES

'''class Ejemplo():
    __atributo_privado = "Soy un atributo inalcanzable desde fuera"

    def __metodo_privado(self):
        print("Soy un metodo inalcanzable desde fuera")

    def metodo_publico(self):
        return self.__metodo_privado()
    
    #GETTER
    @property
    def ver_valor(self):
        print("ESTOY EN EL GETTER")
        return self.__atributo_privado
    
    # SETTER
    @ver_valor.setter
    def ver_valor(self,nuevoValor):
        print("ESTOY EN EL GETTER")
        self.__atributo_privado = nuevoValor

# Programa principal (fuera de la clase Ejemplo)

# probamos a acceder a un atributo como antes y VEMOS QUE DA ERROR
e = Ejemplo()
#print(e.atributo_privado)

#probamos a acceder al atributo con nombre que le hemos puesto en el GETTER
print(e.ver_valor)
'''

## EJEMPLO 9 ENCAPSULACION ## GETTERS Y SETTERS con la clase Persona
'''
class Persona():
    __nombre= "Soy un atributo inalcanzable desde fuera"

    def __init__(self,nombre):
        self.nombre = nombre

    #GETTER
    @property
    def nombre(self):
        print ("ESTOY EN EL GETTER")
        return self.__nombre
    #SETTER
    @nombre.setter
    def nombre (self,nuevoNombre):
        print("ESTOY EN EL SETTER")
        self.__nombre = nuevoNombre

p1 = Persona("Carlos")
print(p1.nombre)
'''

### EJEMPLOS HERENCIA ###

## EJEMPLO 1 HERENCIA ##

# creamos la SUPERCLASE DE PRODUCTO
'''
class Producto():

    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t{}
PVP\t\t{}
DESCRIPCION\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion)

# ahora vamos a crear las subclases, que tendran como CLASE PADRE a PRODUCTO.
class Adorno(Producto): # no tiene ningun atributo o metodo adicional, x lo que hereda todos los atributos y metodos de su padre PRODUCTO
    pass

a = Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con arboles")
print(a)

# seguimos creando la subclase ALIMENTO:
class Alimento(Producto): # NO NECESITA CONSTRUCTOR XQ TIRA DE SU PADRE
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t{}
PVP\t\t{}
DESCRIPCION\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)

al= Alimento(2035,"Botella de aceite",5,"250 ML")
al.productor = "La Aceitera"
al.distribuidor = "Distribuciones SA"
print(al)

# y finalizamos creando la subclase libro
class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t{}
PVP\t\t{}
DESCRIPCION\t{}
ISBN\t{}
AUTOR\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)

l1 = Libro(2036,"Cocina Mediterranea",9,"Recetas sanas y buenas")
l1.isbn = "0-123456-78-9"
l1.autor = "Doña Juana"
print(l1)
'''

## EJEMPLO 2 HERENCIA ## el mismo de arriba  pero todo junto
'''
class Producto():
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t{}
PVP\t\t{}
DESCRIPCION\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion)

class Adorno(Producto): 
    pass

class Alimento(Producto): 
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t{}
PVP\t\t{}
DESCRIPCION\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)

class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t{}
PVP\t\t{}
DESCRIPCION\t{}
ISBN\t{}
AUTOR\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)

# Vamosa crear objetos
ad = Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con arboles")

al= Alimento(2035,"Botella de aceite",5,"250 ML")
al.productor = "La Aceitera"
al.distribuidor = "Distribuciones SA"

l1 = Libro(2036,"Cocina Mediterranea",9,"Recetas sanas y buenas")
l1.isbn = "0-123456-78-9"
l1.autor = "Doña Juana"

# ahora vamos a LISTAR los productos
productos = [ad,al,l1]
print(productos) # recordar que solo con el print nos muestras los objetos en python, NO NOS DEVUELVE UN STRING

# para poder ver todos los elementos debermos usar bucle FOR
for p in productos:
    print(p,"\n")

# Tambien podemos acceder a los atributos si son compartidos entre todos los objetos
for p in productos:
    print(p.referencia,p.nombre)

# pero si un objeto no tiene el atributo deseado nos dara error:
for p in productos:
    print(p.autor)

# Entonces tendremos que tratar cada subclase de forma distina, gracias a la funcion ISINSTANCE --> si es un objeto de la clase Adorno-Alimento,Libro
# es el mejor recurso que tenemos xa filtrar y MUY UTIL xa LISTAR
for p in productos:
    if(isinstance(p, Adorno)):
        print(p.referencia,p.nombre)    
    elif(isinstance(p,Alimento)):
        print(p.referencia,p.nombre,p.productor)
    elif(isinstance(p,Libro)):
        print(p.referencia,p.nombre,p.isbn)
        '''
        

## EJEMPLO 3 HERENCIA ahora con VEHICULOS ## 

class Vehiculos():
    ''' Clase Vehiculo. Incluye la marca y el modelo de un vehiculo. Por defecto el vehiculo no esta en marcha,ni acelerando'''

    # CONSTRUCTOR
    def __init__ (self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    # Metodos de la clase
    def arrancar(self):
        ''' Metodo arrancar() de la clase Vehiculos. Indica al sistema que el vehicula esta en marca'''
        self.enmarcha = True

    def acelerar(self):
        ''' Metodo acelerar() de la clase Vehiculos. Indica al sistema que el vehicula esta acelerando'''
        self.acelera = True   

    def frenar(self):
        ''' Metodo frenar() de la clase Vehiculos. Indica al sistema que el vehicula esta frenando'''
        self.frena = True

    def estado(self):
        ''' Metodo estado() de la clase Vehiculos. Indica al sistema el estado del vehiculo'''
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera)

class Moto(Vehiculos):
    '''Clase MOTO que hereda de VEHICULOS'''

    hacer_caballito = ""
    
    def caballito(self):
        ''' Metodo caballito() de la clase Moto. Indica al sistema si la moto esta haciendo caballito'''
        self.hacer_caballito = "Voy haciendo un caballito"

    #Sobreescribimos el metodo estado (OVERRIDING)
    def estado(self):
        ''' Metodo estado() de la clase MOTO (heredando de Vehiculo). Indica al sistema el estado del vehiculo (MOTO)'''
        print("Marca: ",self.marca,"\Modelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera)

class Furgoneta(Vehiculos):
    '''Clase FURGONETA que hereda de VEHICULOS'''
    def carga(self, cargar):
        ''' Metodo carga() de la clase FURGONETA. Indica al sistema si la FURGONETA esta cargada o no'''
        self.cargado = cargar # Este CARGAR esta definiendo un valor booleando y de ahi dependera lo que ponga en linea 559!!!
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"
        
class VElectrico():
    '''Clase VElectricos'''

    # Constructor
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
      ''' Metodo cargarEnergia() de la clase VElectricos. Indica al sistema si el vehiculo electrico esta cargando'''  
      self.cargando=True

class BicicletaElectrica(VElectrico,Vehiculos):
    '''Clase BicicletaElectrica que HEREDA de la clase VEHICULOS y de la clase VElectricos, es decir, herencia multiple'''
    pass

print("MOTO")

# Objeto de la clase MOTO
miMoto = Moto("Honda","CBR")

# Ejecutamos el metodo caballito de la clase MOTO
miMoto.caballito()
print(miMoto.hacer_caballito)
# Ejecutamos el metodo estado de LA CLASE MOTO
miMoto.estado()

print("\nFURGONETA")
# objeto de la clase FURGONETA
miFurgoneta = Furgoneta("Renault","Kangoo")
# Ejecutamos metodos
miFurgoneta.arrancar()
miFurgoneta.estado()
estadoFurgonetaCargada = miFurgoneta.carga(False)
print(estadoFurgonetaCargada)

print("\nBICICLETA ELECTRICA")
# Objeto de la clase BicicletaElectrica
# Al heredar de 2 clases, tiene disponible 2 constructores
miBici = BicicletaElectrica()
print(miBici.autonomia)

#print(help(Vehiculos))
#print(help(Moto))
#
# 
# 
# print(help(BicicletaElectrica))




    
        