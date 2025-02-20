n =[]
r =[]
print ("Cuantos numeros vas a ingresar: ")

nums=int(input())
i= 0
while i<nums:
    print("valor del numero", i + 1)
    valor=int(input())
    n.append(valor)
    i+=1
promedio = sum(n)/ len(n)
print("El promedio de de los numeros es: ", promedio)
for i in range(len(n)):
        for j in range(len(n)):
            if i != j:
             if n[i]== n[j]:
                if n[i] not in r:
                    r.append(n[i])
print("Los numeros repetidos son: ", r)