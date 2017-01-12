#Reescreva a função 'maximo' do exercício 2, que devolve o maior valor dentre dois inteiros recebidos, 
#para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

def maximo(a, b, c):
	if a > b > c:
		maior = a
	elif b > c:	
		maior = b
	else:
		maior = c
	return maior