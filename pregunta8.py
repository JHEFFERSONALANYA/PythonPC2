def factorial (num):
    fact=1
    for i in range (1,num+1):
        fact=fact*i
    return fact
numero=int(input("Ingrese un numero positivo: "))    
respuesta=factorial(numero)
while numero<1:
    numero=int(input("Dato incorrecto, ingrese un numero positivo: "))
print(f"El factorial de {numero} es {respuesta}")


