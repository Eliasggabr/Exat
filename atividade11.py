
total = 0
maisde150 = 0
while True:
    valor = int(input("Digite um valor (0 para sair): "))
    if valor == 0:
        break
    else:
        total += valor  
        if valor > 150:
            maisde150 += 1