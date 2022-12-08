# Escribí un programa que solicite al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada nombre. A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, [usuario]”, donde “[usuario]” se reemplazará por el nombre que el usuario haya ingresado.

'''nombre=input("introduzca el nombre: ")
print("Ahora estás en la matrix," ,nombre)'''

# Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable. A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el resultado de la operación.

'''numero_1=float(input("introduzca un numero: "))
numero_2=int(input("introduzca un numero: "))
suma=numero_1+numero_2
print("la suma de los numeros es ",suma)'''

# Escribí un programa que solicite al usuario dos números y los almacene en dos variables. En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
# A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.

'''numero_1=int(input("introduzca un numero: "))
numero_2=int(input("introduzca un numero: "))
suma=numero_1+numero_2
numero_3=int(input("introduzca un numero: "))
print("El resultado total es  ",suma * numero_3)'''

# 4- Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro.

'''km_recorridos=float(input("cuantos km recorrio?"))
litros_consumidos=float(input("cuantos litros consumio?"))
print("el consumo de combustible/litro es :",km_recorridos/litros_consumidos)'''

# 5-Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_

'''ingresar_temperatura=float(input("introduzca un numero: "))
conversion=5/9 *(ingresar_temperatura-32)
print("la conversion a grades Celsius es :", conversion,"grados Celsius)'''

# 6-Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle el promedio de los tres.
 
'''numero_1=int(input("introduzca un numero: "))
numero_2=int(input("introduzca un numero: "))
numero_3=int(input("introduzca un numero: "))
print("El promedio de los tres es",(numero_1+numero_2+numero_3)/3)'''

# 7- Escribí un programa que solicite al usuario un número y le reste el 15%, almacenando todo en una única variable. A continuación, mostrar el resultado final en pantalla.

'''numero_1=int(input("introduzca un numero: "))
print("el resultado es: ",numero_1 - (numero_1*15)/100)'''

# 8-Escribí un programa que solicite al usuario el ingreso de dos palabras, las cuales se guardarán en dos variables distintas. A continuación, almacená en una variable la concatenación de la primera palabra, más un espacio, más la segunda palabra. Mostrá este resultado en pantalla.

'''palabra_1 =input("escribe una palabra: ")
palabra_2 =input("escribe una palabra: ")
print(palabra_1 +" "+palabra_2)'''

# 9-Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable. A continuación, mostrar en pantalla la primera letra del texto ingresado. Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4) y almacenar este número en una variable llamada indice.
#Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.

'''texto =input("escribe un texto: ")

print(texto[0])

indice=int(input(("introduzca un numero menor que el tamano del texto:" ,len(texto))))

print(texto[indice])'''

# 10-Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año y almacene ese número en una variable. A continuación mostrar en pantalla un valor de verdad (True o False) que indique si el usuario ha visto más de 3 shows.

'''especatculos=int(input("Cuantos musicales ha visto en el año: "))
print(especatculos>3)'''

# 11-Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números, donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro el año (DDMMAAAA). Este dato debe guardarse en una variable con tipo int (número entero). Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.

'''fecha =int(input("escribe una fecha con el formato DDMMAAAA: "))

dia=fecha//1000000
mes=(fecha%1000000)
mes_2=mes//10000
año=fecha%10000

print(str(dia)+"/"+str(mes_2)+"/"+str(año))'''

# 12-Escribí un programa para solicitar al usuario el ingreso de un número entero y que luego imprima un valor de verdad dependiendo de si el número es par o no. Recordar que un número es par si el resto, al dividirlo por 2, es 0.

'''prueba =int(input("escribe un nº entero: "))

print(prueba%2==0)'''

# 13-Escribí un programa que le solicite al usuario su edad y la guarde en una variable. Que luego solicite la cantidad de artículos comprados en una tienda y la guarde en otra variable. Finalmente, mostrar en pantalla un valor de verdad (True o False) que indique si el usuario es mayor de 18 años de edad y además compró más de 1 artículo.

'''edad=int(input("que edad tiene: "))
articulos=int(input("cuantos articulos compro: "))

print(edad>=18 and articulos>1)'''

# 14-Escribí un programa que, dada una cadena de texto por el usuario, imprima True si la cantidad de caracteres en la cadena es un número impar, o False si no lo es.

'''prueba =(input("escribe una cadena de texto: "))

print(len(prueba)%2==0)'''

# 15 -Escribí un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables, y que luego imprima True si la primera palabra es menor que la segunda o False si no lo es.

'''prueba_1 =(input("escribe una cadena de texto: "))
prueba_2 =(input("escribe una cadena de texto: "))

print(prueba_1<prueba_2)'''