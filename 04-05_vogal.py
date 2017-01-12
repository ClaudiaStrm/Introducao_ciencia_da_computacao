#Escreva a função vogal que recebe um único caractere como parâmetro e retorna True se ele for uma vogal e 
#False se for uma consoante.

def vogal(x):
	if x in 'aeiouAEIOU':
		vog = True
	else:
		vog = False
	return vog