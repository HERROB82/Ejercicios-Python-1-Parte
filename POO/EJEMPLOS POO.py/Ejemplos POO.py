

# Clase de Repaso, vemos varios ejemplos:

# AUTOMATIZAR LA ENTRADA DE DATOS A UNA CLASE

'''class Pelicula:

    # Constructor de la clase (al crear la instancia)
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula",self.titulo)



def pedirdatos(): #Creamos funcion para pedir datos
    t = input("Introduzca titulo de pelicula: ")
    d = int(input("Introduzca duracion de pelicula: "))
    l = int(input("Introduzca lanzamiento de pelicula: "))
    return t,d,l # ahora retorno estas variables

if __name__ == "__main__": # con esto ya declaramos que esto es el main y lo separamos de la clase Pelicula y X AQUI EMPIEZA EL PROGRAMA

    listaPeliculas = [] # creo lista de peliculas para ir metiendolas 
    numPeliculas = int(input("Indique cuantas peliculas quiere añadir: "))
    for i in range(numPeliculas): 
        t, d, l =pedirdatos() # con la funcion pedirdatos pedimos los datos y se retorna por lo tanto hay que capturarla con el t,d,l = pedirdatos
        listaPeliculas.append(Pelicula (t,d,l))

    print("="*40)

    for i in listaPeliculas:
        print(i.titulo)'''


## OBJETOS DENTRO DE OBJETOS  ##

class Temperatura:
    def __init__(self,temp,fecha):
        self.temp = temp
        self.fecha = fecha

class Paciente:
    def __init__(self,nombre,temperaturas):
        self.nombre = nombre
        self.temperaturas = temperaturas

t1 = Temperatura(38,"22:00")
t2 = Temperatura(39,"23:00")
t3 = Temperatura(39.5,"00:00")
lista_temp=[t1,t2,t3]

p1 = Paciente("Cristian",lista_temp)
print(p1.nombre)
print(p1.temperaturas) # al ser una lista de objetos 

for i in p1.temperaturas:
    print (i) # me muestra los objetos xq no tengo el STR implementado

for i in p1.temperaturas: 
    print(i.temp) # ahora si me muestra la info

    
       


