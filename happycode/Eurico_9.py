e_zero = 0
def divisao ():
    a = int(input("Insira o primeiro número: "))
    b = int(input("Insira o segundo número: "))
    while b==0:
        print("A divisão por zero não é válida. Pergunte à Siri!")
        b = int(input("Insira o segundo número: "))
        
    resultado = a / b
    return resultado


#main
c = divisao()
print(c)


    
