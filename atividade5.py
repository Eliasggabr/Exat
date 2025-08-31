
while True:
    senha = input("Digite uma senha: ")
    if senha != "1234":
        print("A senha está incorreta!")
    elif senha == "1234":
        print("Você saiu do loop")
        break