#Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. 
#Se o número for primo, imprima "primo". Caso contrário, imprima "nao primo".

num = int(input('Informe o número: '))
div = 2 

if num == 1:
	print("nao primo")
else:
	while num%div != 0:
		div = div + 1

	if num == div:
		print("primo")
	else:
		print("nao primo")