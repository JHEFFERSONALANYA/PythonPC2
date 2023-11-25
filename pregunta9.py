frase=input("Ingrese su palabra o frase: ")
frase2=''
vocales=['a','e','i','o','u','A','E','I','O','U']
for letras in frase:
    if letras not in vocales:
        frase2=frase2 + letras
print(frase2)

