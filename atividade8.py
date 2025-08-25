
contador = 0 
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    contador += 1
print(f"Foram digitados {contador} números.")