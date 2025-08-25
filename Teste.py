
print("Tabuada") 
while True: 
    num = int(input("Digite um número: "))
    for n in range(1,11):
        result = num * n
        print(f"{num} x {n} = {result}")
    opção = input("Deseja continuar? (s/n): ")
    if opção == "n":
            print("Programa encerrado.")
            break
    elif opção == "s":
            continue
    else:
            print("Opção inválida. Programa encerrado.")
            break