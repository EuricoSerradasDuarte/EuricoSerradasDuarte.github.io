a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))
c = int(input("Insira o terceiro número: "))
d = int(input("Insira o quarto número: "))
soma_pares = 0
soma_impares = 0

if a%2==0:
    soma_pares=soma_pares+a
else:
    soma_impares=soma_impares+a

if b%2==0:
    soma_pares=soma_pares+b
else:
    soma_impares=soma_impares+b

if c%2==0:
    soma_pares=soma_pares+c
else:
    soma_impares=soma_impares+c

if d%2==0:
    soma_pares=soma_pares+d
else:
    soma_impares=soma_impares+d

print("")    

print("A soma dos números pares é", soma_pares)
print("A soma dos números ímpares é", soma_impares)

if soma_pares>=soma_impares:
    print("Tu és um nabo!")
else:
    print("Tu não és um nabo!")
    
