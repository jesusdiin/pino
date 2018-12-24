import math

max = 21
separacion = 5
j = 1

print ("\n\tFELIZ NAVIDAD AMIGOS")

#creacion del pino
for i in range (0,  max,  2) :
    #espacios
    linea = (separacion + math.ceil (max / 2) - j) * " "
    
    #asteriscos
    linea += i * "*"
    
    j += 1
    print (linea)
#creacion del tronco para el pino
linea = (separacion + math.ceil (max / 2) - 3) * " "
linea += 4 * "*"
print (linea)
print (linea)
