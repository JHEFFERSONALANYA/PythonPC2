opcion=input('¿Desea ingresar un numero?: ')
cant1=0
cant2=0
numeros=[]
while opcion=='si' or opcion=='SI':
    num=int(input('Ingrese un numero:')) 
    if  num%2==0:
        cant1+=1
    else: 
        cant2+=1       
    opcion=input('¿Desea ingresar un numero?: ')
    numeros.append(num)
print(f"Los numeros ingresados son: {numeros}")         
print(f"La cantidad de numeros pares es: {cant1}")
print(f"La cantidad de numeros impares es: {cant2}")      