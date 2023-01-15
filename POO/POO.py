'''Definición de CLASE: cada clase es un modelo que define un conjunto de atributos (variables o propiedades), y métodos apropiados para operar con dichos atributos (el comportamiento).
Cada objeto creado a partir de la clase se denomina instancia de clase. Las clases son un pilar fundamental de la POO.
Con la clase definimos a grandes rasgos lo que tendrán el objeto y serán los objetos los que se adapten a esa clase, se convierten en objetos de nuestra clase.
¡¡Esos objetos tendrán las propiedades que les haya dicho la clase!! ¡Podrá hacer lo que la clase le diga lo que puede hacer!
Nuestro trabajo es crear esas clases y saber definirlas.'''

''' Atributos y métodos de clase.
•	Atributos: Hacen referencia a las variables internas de la clase.
•	Métodos: Hacen referencia a las funciones internas de la clase. Métodos son las acciones'''

''' Definición de atributos en clase '''
'''class Galleta():
    chocolate = False

g = Galleta()

print(g.chocolate)
#Con esto todas mis galletas vendrán con el atributo de False (no chocolate) pero si lo necesitamos lo podemos cambiar de la siguiente manera
g.chocolate = True
print(g.chocolate)'''

''' Método init() -> cada vez que veamos un método init es un constructor
Es un método especial de Python para construir un objeto, siempre se ejecuta cuando el objeto se crea por lo que todo lo que queramos que se convierta en ese objeto lo meteremos en el constructor.
SIEMPRE vamos a programar el init(), ya que por poco que vaya a hacer nuestra clase hará algo por lo que tendremos que programar con el método INIT().
¡Solo puede haber un método INIT() por clase!'''

#Ejemplo:

'''class Galleta ():
    chocolate = False

    def __init__(self):
        print("Se acaba de crear una galleta")

g = Galleta()'''

'''Definición de constructores
Un constructor es una subrutina cuya misión es inicializar un objeto de una clase. En el constructor se asignan los valores iniciales del nuevo objeto.
Por ejemplo, cuando se cree un objeto de clase coche, es decir, uno nuevo, lo lógico seria inicializarlo con 4 ruedas:
miCocheNuevo.numRuedas = 4
Variable “self”
La variable self es una variable que hace referencia a una instancia de la misma clase. Hay que declararlo explícitamente como el primer argumento de método para acceder a las variables y métodos de la instancia.

A una función cuando está dentro de una clase se la considera un “método”.'''

# Como vimos ,self, sirve para hacer referencia a los métodos y atributos de su misma clase:

class Galleta ():
    chocolate = False

    def  __init__(self):
        print("Se acaba de crear una galleta")

    def chocolate (self):
        print("Vamos a chocolatear la galleta")
        self.chocolate = True

    def tiene_chocolate(self):
        if self.chocolate == True:
            print("Soy una galleta chocolateada")
        else:
            print("Soy una galleta sin chocolate")

g=Galleta()
g.tiene_chocolate()
g.chocolate()




