nombre = input("Introduce tu nombre: ")
#Comentario
print(f"Hola {nombre}")
#entero
edad=25

#flotante-decimales
altura=1.75

#Convertir a flotante
edadString =str(edad)

#Bolleanos
bolleanos = false

print(edad + edad)
print(edadString + edadString)

print(type(edad))
print(type(edadString))


tuEdad= input("Introduce tu edad: ")

tuEdad= int(tuEdad)

if tuEdad >= 18 and tuEdad < 100:
    print("Eres mayor de edad")
    elif tuEdad >= 100:
        print("¿Eres inmortal?")
        elif tuEdad <=0:
            print("No existes")
    else:
        print("Eres menor de edad")

#Estructura de ctr for
  for i in rango(0,10):
      print(i)      
#Estructura de ctr switch
dia = input("Introduce un dia: ")
dia = int(dia)

with switch(dia) as s:
   if s.case(15):
       print ("Es quincena ")
