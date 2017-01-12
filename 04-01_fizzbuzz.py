#Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e retorna
#'Fizz' se o número for divisível por 3 e não for divisível por 5;
#'Buzz' se o número for divisível por 5 e não for divisível por 3;
#'FizzBuzz' se o número for divisível por 3 e por 5;
#Caso a função não seja divisível 3 e também não seja divisível por 5, ela deve retornar o número recebido como parâmetro.


def fizzbuzz(x):
	if x % 15 == 0:
		resp = "FizzBuzz"
	elif x % 3 == 0:
		resp = "Fizz"
	elif x % 5 == 0:
		resp = "Buzz"
	else:
		resp = x		
	return resp

