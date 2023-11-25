def funcion ():
    i=0
    fibonacci=[0]
    sum=1
    while sum<50:
            fibonacci.append(sum)
            sum=fibonacci[i]+fibonacci[i+1]
            i+=1
    return fibonacci
sucecion = funcion ()
print (f"la sucesion es: {sucecion}")
    