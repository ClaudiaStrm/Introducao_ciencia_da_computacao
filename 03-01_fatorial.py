# Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.
n = int(input("Digite o valor de n: "))
fat = 1

for x in range(1, n+1):
	fat = fat * x
print(fat)