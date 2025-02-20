n =[]
r =[]
print ("Cuantos numeros vas a ingresar: ")

n=int(input())
i= 0
while i<n:
    print("valor del numero", i + 1)
    valor=int(input())
    n.append(valor)
    i+=1
promedio = sum(n)/ len(n)
print("El promedio de de los numeros es: ", promedio)
for i in range(len(n));
for r in range(len(n)):
    if i != r:
        if n[i]== n[r]:
            if n[i] not in r:
                r.append(n[i])
print("Los numeros repetidos son: ". r)