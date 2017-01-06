'''O programa deve receber os parâmetros a, b, e c da equação ax2+bx+c, respectivamente, 
e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima: esta equação não possui raízes reais

Quando houver apenas uma raiz real imprima: a raiz desta equação é  onde X é o valor da raiz

Quando houver duas raízes reais imprima: as raízes da equação são X e Y onde X e Y são os valor das raízes.

Além disto, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente, ou seja, 
X deve ser menor ou igual a Y.
'''

import math

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))

delta = b ** 2 - 4 * a * c

if a == 0 or delta < 0:
	print("esta equação não possui raízes reais")
elif delta == 0:
	raiz1 = (- b )/ (2 * a)
	print("a raiz desta equação é %.3f" %raiz1)
else:
	raiz1 = (- b + math.sqrt(delta)) / (2 * a)
	raiz2 = (- b - math.sqrt(delta)) / (2 * a)

	a = min(raiz1, raiz2)
	b = max(raiz1, raiz2)
	print("as raízes da equação são %f e %f" %(a, b))	