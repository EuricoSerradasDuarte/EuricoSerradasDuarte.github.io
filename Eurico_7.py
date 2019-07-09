escolha = int(input("Insira um número: "))
resultado = escolha
repeticoes = 1
while escolha>repeticoes + 1:
    resultado = resultado*(escolha-repeticoes)
    repeticoes = repeticoes + 1
print(resultado)
