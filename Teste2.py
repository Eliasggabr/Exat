
contador = 0 
vogais = 'aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛãõÃÕäëïöüÄËÏÖÜ'
palavra = input("Digite uma palavra: ")
for letra in palavra:
    if letra in vogais:
        contador += 1
print(f"A palavra '{palavra}' tem {contador} vogais.")  
