#Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui 
#ao menos um dígito com um dígito adjacente igual a ele. 
#Caso exista, imprima "sim". Se não existir, imprima "nao".

x = input("Digite o número: ")
n = 0

if len(x) == 1:
	print("nao")
else:
	while True:
		if n == (len(x) - 1):
			print("nao")
			break
		if x[n] == x [n + 1]:
			print("sim")
			break
		n += 1
