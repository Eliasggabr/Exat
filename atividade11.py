
total = 0
maisde150 = 0
while True:
    valor = int(input("Digite um valor (0 para sair): ")) 
    total += valor 
    if valor > 150:
            maisde150 += 1
    if valor == 0:
        print(f"O valor é de R${total}! Têm {maisde150} produtos com mais de R$150.")
        break