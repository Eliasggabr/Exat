
print("Tabuada")
num = int(input("Digite um número: "))
while True:
    for i in range(1,11):
        result = num * i
        print(f"{num} x {i} = {result}")
    opção = input("Deseja continuar? (s/n): ")
    if opção == "n":
            print("Programa encerrado.")
            break
    elif opção == "s":
        continue
    else:
        print("Opção inválida. Programa encerrado.")
        break