#Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.

n = int(input("Digite um número inteiro: "))

x = n // 10
x = x % 10

print("O dígito das dezenas é %s" %x)