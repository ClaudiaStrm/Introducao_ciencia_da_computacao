#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e 
#retorna o maior número primo menor ou igual ao número passado à função

def maior_primo(x):
	for i in range(2, (x+1)):
		div = 2 
		while i%div != 0:
			div = div + 1
		if i == div:
			mprimo = i
	return mprimo