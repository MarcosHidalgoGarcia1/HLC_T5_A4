#Va multiplicando todos los numeros que van antes del numero ingresado (en este caso del 5 (1*2*3*4*5))

#Iterativa
def Factorial(n):
     
     resultado=1
     
     for i in range(1, n+1):
         resultado*=i
     return resultado

print(Factorial(5))

#Recursiva
def Factorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n-1)

print(Factorial(5))
