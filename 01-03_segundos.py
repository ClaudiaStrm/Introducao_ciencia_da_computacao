#Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python 
#que dada a quantidade de segundos, o programa "quebra" esse valor em dias, horas, minutos e segundos.

tempo = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = tempo / 3600 / 24

if dias > 0:
	segs = tempo - 86400 * int(dias)
	horas = segs / 3600
else: 	
	horas = tempo / 3600

minutos = (tempo % 3600) / 60
segundos = (tempo % 60)

print("%d dias, %d horas, %d minutos e %d segundos." %(dias, horas, minutos, segundos))