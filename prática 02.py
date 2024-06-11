#ATIVIDADES#
#int- números inteiros
#float- números decimais
#bool- boleano (sim/não)
#str- texto

#DESAFIO 1
# Crie um programa que leia dois números e mostra a soma entre eles.    
numero1= int(input("Digite um numero:")) 
numero2= int(input("Digite outro numero:"))
soma= numero1+numero2
print("Soma =", soma)

#DESAFIO 2
# Faça um programa que leia um número inteiro e mostra na tela e seu sucessor e seu antecessor.
numeroInteiro= int(input("Digite um número:"))
sucessor= numeroInteiro+1
antecessor= numeroInteiro-1
print("numero antecessor:", antecessor)
print("numero sucessor:", sucessor)

#DESAFIO 3
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e o seu quadrado.
numero3=int(input("Digite um número:"))
print(f"O dobro desse número é {numero3*2},seu triplo é {numero3*3} e seu quadrado é {numero3**2} ")

#DESAFIO 4
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostra a sua média.
nota1=int(input("Digite a primeira nota: "))
nota2=int(input("Digite a segunda nota: "))
print(f"A média das duas notas é: {(nota1+nota2)/2}")

#DESAFIO 5 
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares. Ela pode comprar.Considere o dólar = R$ 5,00
dinheiro=int(input("Quanto dinheiro você tem na carteira?"))
print(f"Você possui {dinheiro/5} dólares")

#VAMOS PRATICAR
#1.Crie um programa para efetuar a eitura de um número inteiro e apresentar esse resultado ao quadrado
numero4=int(input("Digite um número inteiro:"))
print(f"O resultado ao quadrado desse número é: {numero4**2}")

#2. Crie um programa que leia dois caracteres e imprima-os na tela da seguinte forma: "O úsuario digitou {caractere1} e {caractere2}!"
numero5= str(input("Digite o primeiro caractere:"))
numero6= str(input("Escreva o segundo caractere:"))
print(f"O usuário digitou {numero5} e {numero6}!")

#3. Crie um programa para entrar com a base e a altura de um retângulo e imprima respectivamente o perímetro e a área correspondente
base= int(input("Qual é a base do retângulo?"))
altura= int(input("Qual é a altura do retângulo?"))
print(f"O perímetro desse retângulo é: {(2*base)+(2*altura)}, e a área é {base*altura}")

#4. Crie um programa que valor, taxa e o tempo, efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula PRESTAÇÃO=VALOR+(VALOR*(TAXA/100)*TEMPO)
valor= int(input("Qual é o valor da prestação?"))
taxa= int(input("Qual é a taxa da prestação?"))
tempo= int(input("Qual é o tempo em dias das prestações?"))
prestacao= valor+(valor*(taxa/100)*tempo)
print(f"O valor da prestação atrasada é:{prestacao}")