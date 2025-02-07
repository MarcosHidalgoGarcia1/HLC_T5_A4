#Hace la suma de los numeros que pone el usuario (en este caso de 1234)
def suma(n):
    if n == 0:
        return 0 
    return n%10 + suma(int(n/10))
print(suma(1234))

# 1a iteracion: n=1234 -> n%10=4 + suma(1234/10=123)
# 2a iteracion: n=123 -> n%10=3 + suma(123/10=12)
# 3a iteracion: n=12 -> n%10=2 + suma(12/10=1)
# 4a iteracion: n=1 -> n%10=1 + suma(1/10=0)
# 5a iteracion: n=0 -> 0