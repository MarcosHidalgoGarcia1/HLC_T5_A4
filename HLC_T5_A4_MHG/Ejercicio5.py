#Contador que cuenta cuantos dígitos tiene lo que pone el usuario (en este caso 1234)
def contar(n):
    if n < 10:
        return 1
    return 1 + contar(n/10)

print(contar(1234))
    