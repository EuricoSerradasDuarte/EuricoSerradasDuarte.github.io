print("Olá!")
print("Insira a letra correspondente à sua escolha.")
print("Soma de números: s")
print("Concatenação de frases: c")
print("Idade: i")
escolha = str(input("Escreva aqui: "))
if escolha == "s":
    print("")
    primeiro = int(input("Escolhe o primeiro número: "))
    segundo = int(input("Escolhe o segundo número: "))
    print("O seu número é", str(primeiro + segundo))
    exit

if escolha == "c":
    print("")
    frase_primeira = input("Escolhe a primeira frase: ")
    frase_segunda = input("Escolhe a segunda frase: ")
    print("A sua frase final é: ", "'"+frase_primeira, frase_segunda+"'")
    exit

if escolha == "i":
    print("")
    nascimento = int(input("Escolhe o seu ano de nascimento: "))
    atual = int(input("Escolhe o ano atual: "))
    print("Tens, atualmente,", str(atual-nascimento), "anos")
