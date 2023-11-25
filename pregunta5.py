def contar (numero,digito):
        c=0
        while numero>0:
                if digito==numero%10:
                        c+=1
                numero=numero//10
        return c 
a=int(input("Ingrese un numero: "))
b=int(input("Ingrese el digito que quiere contar: "))
count=contar(a,b)
print(f"La cantidad de veces que se repuite el digito '{b}' es: {count}")