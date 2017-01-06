#Receba 4 números inteiros na entrada. 
#Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. 
#Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
#Calcule a distância entre os dois pontos. 
#Se a distância for maior ou igual a 10, imprima longe na saída. 
#Caso o contrário, quando a distância for menor que 10, imprima perto

from math import sqrt


xA = int(input("Informe o primeiro valor de X: "))
yA = int(input("Informe o primeiro valor de Y: "))
xB = int(input("Informe o segundo valor de X: "))
yB = int(input("Informe o segundo valor de Y: "))

d = sqrt(((xB - xA) ** 2 ) + ((yB - yA) ** 2))

if d <= 10:
	print("perto")
else:
	print("longe")
