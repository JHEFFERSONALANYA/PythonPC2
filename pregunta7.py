def cant_div (num):
    contador=2
    for i in range (2,num):
        if num%i==0:
            contador+=1
    return contador             
numero=int(input("Ingrese un numero positivo: "))
divisores= cant_div (numero)
if divisores<=2:
        print(f"El numero {numero} es primo")  
else:
        print(f"El numero {numero} no es primo")
