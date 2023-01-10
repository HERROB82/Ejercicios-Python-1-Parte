# 1- Escribe un programa que permite generar la tabla de multiplicar de un numero entero positivo N, comenzando desde 1.
# Si el programa escribe un numero incorrecto, el programa no se ejecuta. En cambio,  pregunta de nuevo por la informacion hasta que el dato ingresado sea correcto.

'''comprobar=True #creamos variable y la inicializamos como verdadera

while comprobar==True: #creamos un ciclo que  mientras que while sea verdadera se ejecuta todo lo de abajo.

    n=int(input("Ingrese un numero entero positivo: "))

    if n > 0:        
        for i in range (1,11):
            print(n,"por",i,"es igual a",n*i)

        comprobar=False # con esto lo que hacemos es cambiar el estado de la variable que esta ejecutando el bucle While

    else:
        print("Debe introducir un numero entero positivo.Intentelo nuevamente")'''

# 2- Escribe un programa que, al recibir como dato un numero entero positivo N, calcule el resultado de la siguiente serie:
#   1+(1/2) + (1/3) + (1/4) + ...(1/N)

'''comprobar=True

while comprobar ==True:

    n=int(input("Ingrese un numero entero positivo: "))

    if n > 0:
        comprobar = False
        resultado = 0

        for i in range (1,n+1):
            resultado = resultado + (1/i) #resultado += (1+i)
            print("El resultado de la variable es: ",resultado)

    else:
        print("el numero ingresado no es correcto.Intentelo nuevamente")'''

# 3- Escribe un programa que, al recibir como dato un numero entero positivo N, calcule el resultado de la siguiente serie:
#   1/(1/2) * (1/3) / (1/4) * ... (*/) (1/N)

'''comprobar=True

while comprobar==True:

    n=int(input("Ingrese un numero entero positivo: "))

    if n > 0:

        comprobar=False

        resultado = 1
        for i in range(2,n+1):
            if i%2==0:
                resultado=resultado / (1/i)
            else:
                resultado=resultado * (1/i)

        print("el resultado de la serie es: ",resultado)    

    else:
        print("el numero ingresado no es correcto.Intentelo nuevamente")'''


# Construye un programa que, el recibir como datos el peso, la altura y el genero de N personas que pertenecen a un estado de un pais, obtenga el promedio del peso y el promedio de la altura, tanto de la poblacion masculina como de la femenina.






