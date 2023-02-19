# Empezamos con el ejemplo de Herencias:

# Definimos de forma normal y corriente la clase PRODUCTO

# SUPERCLASE PRODUCTO
'''class Producto():
    def __init__(self,idproducto,nombre,precio,descripcion):
        self.idproducto = idproducto
        self.nombre = nombre
        self.precio = precio
        self.descricpion = descripcion
        print("Constructor de la clase Producto")

    def __str__(self):
        return """--> PRODUCTO <--
                - IdProducto : {}
                - Nombre: {}
                - Precio: {}
                - Descripcion: {}""".format(self.idproducto,self.nombre,self.precio,self.descricpion)

# SUBCLASE ALIMENTO
class Alimento (Producto):
    productor =""   # al no crear constructor tengo que meter toda la info metiendole todos los argumentos abajo
    distribuidor ="" # y luego asiganrle valores a "productor" y a "distribuidor"
                    # Aqui Alimento tira de Producto ya que al no tener constructor propio tira del de "PRODUCTO"
    def __str__(self):
        return """--> PRODUCTO ALIMENTO <--
                - IdProducto : {}
                - Nombre: {}
                - Precio: {}
                - Descripcion: {}
                - Productor: {}
                - Distribuidor: {} """.format(self.idproducto,self.nombre,self.precio,self.descricpion,self.productor,self.distribuidor)

al = Alimento(48975,"Botella de Aceite de Oliva Extra",5,"250 ML")
al.productor = "La Aceitera"
al.distribuidor = "Distribuciones SA"
print(al)

# SUBCLASE LIBRO
class Libro (Producto):
    isbn =""  
    autor ="" 
                    
    def __str__(self):
        return """--> PRODUCTO LIBRO <--
                - IdProducto : {}
                - Nombre: {}
                - Precio: {}
                - Descripcion: {}
                - ISBN: {}
                - Autor: {} """.format(self.idproducto,self.nombre,self.precio,self.descricpion,self.isbn,self.autor)

li = Libro(15897,"Cocina Japonesa",15,"Recetas de oriente")
li.isbn = "1265626526856"
li.autor = "Maestro Sun"
print(li)

# SUBCLASE ROPA
class Ropa (Producto):
    talla =""  
    marca ="" 
                    
    def __str__(self):
        return """--> PRODUCTO ROPA <--
                - IdProducto : {}
                - Nombre: {}
                - Precio: {}
                - Descripcion: {}
                - Talla: {}
                - Marca: {} """.format(self.idproducto,self.nombre,self.precio,self.descricpion,self.talla,self.marca)

ro = Ropa(11236,"Jersey Fit 18",18,"Jersey de hombre de invierno") #estas clases se construyen con el constructor padre con los 4 argumentos
ro.talla = "36" # y nosotros de manera manual tenemos que poner estos dos indicandole estos atributos extras
ro.marca = "Guci" # y nosotros de manera manual tenemos que poner estos dos indicandole estos atributos extras
print(ro)

# Creamos LISTA de PRODUCTOS
productos = [al,li,ro]
print(productos)'''

# Uso del SUPER

# Hasta ahora hemos definido las clases hijas sin constructor,de tal modo, cuando instanciamos un objeto de estas clases hijas, usan el 
# constructor del padres para construirse. Este mecanismo puede estar bien cuando nuestras clases hijas no tienen atributos especificos o 
# tienen muy pocos, y su forma de crearse es muy similar al del padre. Pero ¿ que pasa cuando una clase hija tiene muchos atributos 
# propios o su forma de crearse difiere mucho de la forma de su padre? EN ESTE CASO UTILIZAMOS EL METODO SUPER().

# El metodo SUPER() invocado desde una clase hija, hace referencia al padre. Por lo tanto, SUPER() solo funciona cuando tenemos una 
# estructura de herencia.

# Podemos utilizar SUPER() con el sig. formato: super().cualquier_metodo_de_la_clase_padre()
# Veamos un ejemplo a continuacion, la clase Alimento que hereda de Producto tiene su propio constructor,donde realiza dos tareas:
# 1) Definir sus atributos propios (Productor y Distribuidor)
# 2) Invocar al constructor del padre con SUPER().init() y enviarle por parametro los atributos comunes q pertenecen a la clase del 
# padre (referencia,nombre,pvp y descripcion)

# Es muy importante que el numero y orden de los parametros que enviamos desde el hijo (con super.init()) al padre, sean los mismos
# en numero y orden que los que hay definidos en el constructor padre.
# Vamos a verlo con un ejemplo:

'''class Producto():
    def __init__(self,idproducto,nombre,precio,descripcion):
        self.idproducto = idproducto
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        print("Constructor de la clase Producto")

    def saludar(self):
        print("Buenos dias")

class Alimento(Producto):
    def __init__(self,idproducto,nombre,precio,descripcion,productor,distribuidor):
        super().__init__(idproducto,nombre,precio,descripcion)# invocamos al constructor de mi padre y le envio todo lo que no quiero
        self.productor = productor # y nos quedamos con lo que si queremos
        self.distribuidor = distribuidor # y nos quedamos con lo que si queremos
        print("COnstructor de la clase Alimento")
        super().saludar()

alimento1 = Alimento(2035,"Botella de aceite",5,"250 ML","La Aceitera","Distribuciones SA")
print(alimento1.nombre)
alimento2 = Alimento (idproducto=2036,nombre="Vinagre",descripcion="Vinagre exra",productor="La Vinagrera",distribuidor="Distribuicones SL")
print(alimento2.nombre) #da error porque no pusimos todos los argumentos, ahora es cuando pondria NONE arriba en todos los argumentos
# y para saber si el precio'''

# BONUS: Comprobar si una clase hereda de otra

class Vehiculo:
    pass

class Coche(Vehiculo):
    pass

class Gato:
    pass

print(issubclase(Coche,Vehiculo))
print(issubclase(Gato,Vehiculo))








