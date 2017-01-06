#Receba um número inteiro na entrada e imprima Fizz se o número for divisível por 3. 
#Caso contrário, imprima o mesmo número que foi dado na entrada.7

x = int(input("Informe o número: "))

if x % 3 == 0:
	print("Fizz")
else:
	print(x)