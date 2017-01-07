#Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma 
#dos dígitos deste número na saída

x = input("Informe o número: ")
s = 0
for n in range(0, len(x)):
	s += int(x[n])

print(s)

