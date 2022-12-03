#1.	¡¡¡¡¡¡¡¡¡¡   Ejercicios de TIPOS DE DATOS SIMPLES 1ºParte     !!!!!!!

#1.1	Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!

#print("Hola Mundo")

#1.2	Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

#prueba="Hola Mundo"
#print(prueba)

#1.3	Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

#nombre=input("Introduzca un nombre: ")
#print("Hola",nombre)


#1.4	Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética (3+22⋅5)2.

#prueba = (3+2*5)/2
#print(prueba)

#1.5	Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

#horas=int(input("Introduzca nº de horas trabajadas: "))
#coste=int(input("Introduzca coste por horas: "))
#resultado=horas * coste
#print("la paga que le corresponde es:",resultado)

#1.6	Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

#n=int(input("Introduzca un numero: "))
#while n<= 0:
#  n=int(input("Introduzca un numero positivo: "))
#  resultado= ((n+1)*n)/2
  
#print(resultado)


#1.7	Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

#peso=float(input("Introduzca su peso: "))
#altura=float(input("Introduzca su altura: "))
#imc=peso/altura
#print("Tu indice de masa corporal es ",float(round(imc,2)))

#1.8	Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

'''n=int(input("Introduzca un nº: "))
m=int(input("Introduzca un nº: "))
c=n//m
r=n%m
print("la division de {} entre la {} da un cociente {} y un resto {} donde N y M son los numeros introducidos por el usuario y C y R son el resultado".format(n,m,c,r))'''

#1.9	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

'''cantidad=float(input("Introduza su cantidad: "))
interes_anual=float(input("Introduzca el interes: "))
duracion=int(input("introduzca cantidad de meses: "))
inversion = (cantidad*interes_anual)/duracion
print("El capital obtenido es:",inversion,"euros")'''

#1.10	Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

'''art_payaso= 112
art_muneca= 75
venta_payaso=int(input("Cantidad payasos vendidos: "))
venta_muneca=int(input("Cantidad muneca vendidos: "))
total_payaso=art_payaso * venta_payaso
total_muneca=art_muneca * venta_muneca
print("el peso total del paquete es de: ",total_payaso + total_muneca)'''



#1.11	Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

'''interes= 0.04
monto_incial=float(input("Introduzca monto inicial: "))
a=round((monto_incial * interes) + monto_incial)
b=round((a * interes) + a)
c=round((b * interes) + b)


print("Tu ahorro del primer año es {}, del segundo es {} y del tercer año es del {}.".format(a,b,c))'''
   

#1.12	Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

'''pan_dia=3.49
descuento_pan_no_dia=3.49 * 0.60
numero_barras=int(input("Introduzca barras NO del dia vendidas: "))
coste_total= round((pan_dia * numero_barras) + ((pan_dia*descuento_pan_no_dia)*numero_barras))

print("el numero de barras habitual es de {}, el descuento de una barra es de {} y el coste final total de la panaderia es de: {}".format(numero_barras,descuento_pan_no_dia,coste_total))'''



#2.	¡¡¡¡¡¡¡¡¡¡   Ejercicios con CADENAS     !!!!!!!

#2.1. Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

'''nombre=input("Cual es tu nombre: ")
numero=int(input("Introduzca un numero: "))
print((nombre +"\n") * numero)'''

#2.2.Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

'''nombre=input("Cual es tu nombre: ")
apellido=input("Cual es tu apellido: ")

print(nombre.lower(),apellido.lower())
print(nombre.upper(),apellido.upper())
print(nombre.capitalize(),apellido.capitalize())'''

#2.3. Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

'''nombre=input("Cual es tu nombre: ")
largo_nombre=len(nombre)
print("{} tiene {} letras".format(nombre,largo_nombre))'''

#2.4. Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

'''telefono = input("Introduzca numero de telefono con prefijo y extension +34 xxxxxxxxx - xx: ")
print("el numero de telefono es ",telefono[4:])'''

#2.5. Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

'''frase=input("Introduzca una frase cualquier: ")
print(frase[::-1])'''

#2.6. Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

'''frase=input("Introduzca una frase cualquier: ")
vocal=input("Introduzca una vocal cualquier: ")
print(frase.replace(vocal,vocal.upper()))'''

#2.7. Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

'''correo=input("Introduzca su direccion de mail: ")
parte_1=correo.split("@")
print(parte_1[0]+"@ceu.es")'''


#2.8. Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

'''consulta_precio=float(input("intorduzca el precio del articulo: "))
print(round(consulta_precio,2))'''

#2.9. Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

'''fecha=input("Introduzca la fecha de su nacimiento en formato dd/mm/aaaa: ")

dia=fecha.split("/")
mes=fecha.split("/")
año=fecha.split("/")
print(dia[0])
print(mes[1])
print(año[2])'''

#2.10. Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

'''cesta=input("Introduzca los productos de la cesta utilizando coma: ")
#cesta_2=cesta.replace(",","\n")
#print(cesta_2)

resultado=cesta.split(",")
for x in (resultado):
  print(x)'''

#2.11. Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

'''producto=input("introduzca el nombre del producto: ")
precio=float(input("introduzca su precio: "))
unidades=int(input("introduzca el numero de unidades: "))
coste_total=round(precio * unidades,2)

print("el producto es {}, su precio unitario es de {}, el numero de unidades es {} y el coste total es de {}".format(producto,round(precio,2),unidades,coste_total))'''


#3.	¡¡¡¡¡¡¡¡¡¡   Ejercicios con LISTAS [] y TUPLAS ()     !!!!!!!

#4.1. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

'''asignaturas=["Matematicas","Fisica","Quimica"]
print(asignaturas)'''

#4.2. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

'''asignaturas=["Matematicas","Fisica","Quimica"]

for x in asignaturas:
  print("Yo estudio",x)'''

#4.3. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

'''asignaturas=["Matematicas","Fisica","Quimica"]

for asignatura in asignaturas:
  consulta=float(input("Que nota has sacado en " + asignatura + ":"))
  print(asignatura," has sacado la siguiente nota en : ",consulta)'''


#4.4. Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

'''numeros_primitiva=[]
for numero in range(6):
  consulta_numeros=int(input("Introduzca los 6 numeros de la primitiva: "))
  numeros_primitiva.append(consulta_numeros)
numeros_primitiva.sort(reverse=True)
print(numeros_primitiva)'''



#4.5. Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.



#4.6. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.



#4.7. Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.



#4.8. Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.



#4.9. Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.



#4.10. Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.



#4.11. Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.



#4.12. Escribir un programa que almacene las matrices:
 
#en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.



#4.13. Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.


#4.	¡¡¡¡¡¡¡¡¡¡   Ejercicios con Condicionales     !!!!!!!

#4.1. Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

'''edad =int(input("Que edad tiene: "))
if edad >= 18:
  print("es mayor de edad")
else:
  print("es menor")'''
  


#4.2. Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

'''password="contrasena"

password_1=str(input("Introduzca la contraseña: "))

if password_1.lower()==password.lower():
  print("contraseña correcta")
else:
  print("contraseña incorrecta")'''



#4.3. Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

'''num_1=int(input("Introduzca un numero: "))
num_2=int(input("Introduzca un numero: "))

if num_2 == 0:
  print("es un error")
else:
  print("la operacion es: ",num_1/num_2)'''


#4.4. Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

'''num_1=int(input("Introduzca un numero: "))
if num_1 % 2 ==0:
  print("el numero es par")
else:
  print("el numero",num_1,"es impar")'''


#4.5. Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

'''edad= int(input("Introduzca su edad: "))
ingresos=int(input("Introduzca sus ingresos: "))
if edad> 16 and ingresos >= 1000:
  print("debe pringar")
else:
  print("se ha salvado")'''


#4.6. Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

'''nombre=str(input("Introduzca su nombre: "))
sexo=str(input("Introduzca su sexo: "))
if (nombre [0] < "m" and sexo == "femenino") or (sexo == "masculino" and nombre [0] > "n"):
  print("entras en el grupo A")
else:
  print("entras en el grupo B")'''


#4.7. Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

 
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

'''renta_a= 0.5
renta_b= 1.5
renta_c= 2
renta_d= 3
renta_e= 4.5

renta=float(input("introduzca su renta: "))

if renta < 10000:
  print("su tipo impositivo es: ",renta_a)
elif renta <=20000:
  print("su tipo impositivo es: ",renta_b)
elif renta <=35000:
  print("su tipo impositivo es: ",renta_c)
elif renta <=60000:
  print("su tipo impositivo es: ",renta_d)'''
  

#4.8. En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

#puntuacion 0.0 inaceptable
#puntuacion 0.4 aceptable
#puntuacion 0.6 meritorio
 
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

'''puntuacion_1= 0.0 
puntuacion_2= 0.4 
puntuacion_3= 0.6 

desempeño=float(input("cual fue la puntuacion del empleado: "))
if desempeño == puntuacion_1:
  print("no hay bonus este año")
elif desempeño == puntuacion_2:
  print("tu bonus es de :",puntuacion_2 * 2400)
else:
  print("tu bonus es de ",puntuacion_3 * 2400)'''






#4.9. Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

'''edad=int(input("Que edad tiene: "))

if edad == 0 or edad <4:
  print("usted entra gratis")
elif edad >= 4 or edad < 18:
  print("usted paga 5 euros")
else:
  print("usted paga 10 euros")'''


#4.10. La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#•	Ingredientes vegetarianos: Pimiento y tofu.
#•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
