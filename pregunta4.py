cant_alumnos=int(input("Ingrese la cantidad de alumnos en su lista: "))
lista = []
for j in range (cant_alumnos):
    parte={}
    alumno=input("Ingrese el nombre del alumno: ")
    parte[f'ALUMNO {j+1}']=alumno
    notas=[]
    for i in range (3):
        nota_i=int(input(f'Ingrese un la nota {i+1}: '))
        notas.append(nota_i)
    parte['notas']=notas
    lista.append(parte)    
for m in range (cant_alumnos):
    print(f"ALUMNO: {lista[m][f'ALUMNO {m+1}']}")
    print(f"NOTAS: {lista[m]['notas']}")
    print('------------------------------------')

         
