#Listas
milista=["Huevos","Leche","Carne","Jugo"]
print(milista)
print(milista[0])
print(milista[1])
print(milista[2])
print(milista[3])

milista[0]="Cereal"
print(milista)
print(len(milista))

for dato in milista:
    print("Dato: ",dato)

milista.append("Jabon")
print(milista)

milista.insert(1,"Cafe")
print(milista)

milista.remove("Leche")
print(milista)

elemento=milista.pop(0)
print("Saque: ",elemento)
print(milista)

milista.reverse()
print(milista)

milista.sort()
print(milista)

milista.sort(reverse=True)
print(milista)

