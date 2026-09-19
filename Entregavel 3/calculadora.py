def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("Erro: Não é possível dividir por zero.")
        return None
    return a / b


#Versão portugol:

#{
#	// Função para somar dois números
#	funcao real somar(real a, real b)
#	{
#		retorne a + b
#	}
#
#	// Função para subtrair dois números
#	funcao real subtrair(real a, real b)
#	{
#		retorne a - b
#	}
#
#	// Função para multiplicar dois números
#	funcao real multiplicar(real a, real b)
#	{
#		retorne a * b
#	}
#
#	// Função para dividir dois números com tratamento de erro
#	funcao real dividir(real a, real b)
#	{
#		se (b == 0.0) {
#			escreva("Erro: Não é possível dividir por zero.\n")
#			retorne 0.0 // Em Portugol, retornamos um valor padrão de erro
#		}
#		senao {
#			retorne a / b
#		}
#	}
#
#	funcao inicio()
#	{
#		// Teste das funções da calculadora
#		escreva("Soma: ", somar(10.0, 5.0), "\n")
#		escreva("Divisão por zero: ")
#		dividir(10.0, 0.0)
#	}
#}