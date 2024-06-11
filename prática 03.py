#DESAFIO 1
#Crie um programa que leia o nome completo de uma pessoas e mostre:
#1) O nome com todas as letras maiúsculas (.upper)
#2) O nome com todas as letras minúsculas (.lower)
#3) Quantas letras ao todo (sem considerar espaços) (x:0)
#4) Quantas letras tem o primeiro nome
nomeInteiro= input("Digite seu nome completo:")
print(f"Nome maiúsculo: {nomeInteiro.upper()}")
print(f"Nome minúsculo:{nomeInteiro.lower()}")
print(f"Seu nome completo possui: {len(nomeInteiro)} caracteres")
nomeInteiroSemEspaço= nomeInteiro.replace(" " , "")
print(f"Seu nome completo possui: {len(nomeInteiroSemEspaço)} letras")

# # DESAFIO 02
# # Crie um programa que leia o nome de uma cidade e siga se ela começa ou não com o nome “Santo”.
cidade=str(input("Qual é o nome da sua cidade?"))
print(f"{'Santo' in cidade}")

# # DESAFIO 03
# # Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome3=str(input("Digite seu nome:"))
print(f"{'Silva' in nome3}")

# DESAFIO 04
# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez
frase=input("Digite uma frase:")
print(frase.count("a"))
print(f"Letras A:{frase.count('a')}")
print(f"Ela aparece pela primeira vez nessa posição: {frase.find('a')}")
print(f"Ela aparece pela última vez nessa posição: {frase.find('a ')}")

# DESAFIO 05
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome separadamente
# Exemplo: Ana Maria De Souza
# Primeiro: Ana
# Ultimo: Souza
nomeCompleto=input("Digite seu nome completo:")
nomeSeparado= nomeCompleto.split()
print(nomeSeparado)
