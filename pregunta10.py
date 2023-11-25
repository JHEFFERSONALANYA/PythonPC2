fecha=input("Ingrese la fecha: ")
mes_lista=[
"Enero",
"Febrero",
"Marzo",
"Abril",
"Mayo",
"Junio",
"Julio",
"Agosto",
"Septiembre",
"Octubre",
"Noviembre",
"Diciembre"
]
caracter1=fecha.find("/")
caracter2=fecha.find(",")
if caracter1>0:
    [mes,dia,año]=fecha.split("/")
    print(f"{año}-{mes.zfill(2)}-{dia.zfill(2)}")
elif caracter2>0:
    [mes_dia,año]=fecha.split(", ")
    [mes,dia]=mes_dia.split(" ")
    mes=mes_lista.index(mes)+1
    print(f"{año}-{str(mes).zfill(2)}-{dia.zfill(2)}")
    

