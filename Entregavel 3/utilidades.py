# 1. Conversor de temperatura (Celsius para Fahrenheit)
def converter_celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# 2. Validador de senha (mínimo 8 caracteres e pelo menos um número)
def validar_senha(senha):
    tem_tamanho_minimo = len(senha) >= 8
    tem_numero = any(caractere.isdigit() for caractere in senha)
    
    return tem_tamanho_minimo and tem_numero


# 3. Caixa com *precos (*args para aceitar quantidade variável de preços)
def calcular_total_caixa(*precos):
    total = sum(precos)
    return total


# 4. Ficha do Aluno com **dados (**kwargs para aceitar dados flexíveis)
def gerar_ficha_aluno(nome, **dados):
    ficha = f"--- FICHA DO ALUNO: {nome.upper()} ---\n"
    for chave, valor in dados.items():
        # Formata o nome do campo (ex: 'data_nascimento' vira 'Data Nascimento')
        campo = chave.replace("_", " ").title()
        ficha += f"{campo}: {valor}\n"
    return ficha


#Versão Portugol:

#programa
#{
#	// 1. Conversor de temperatura (Celsius para Fahrenheit)
#	funcao real converterCelsiusParaFahrenheit(real celsius)
#	{
#		retorne (celsius * 9.0 / 5.0) + 32.0
#	}
#
#	// 2. Validador de senha (comprimento mínimo e presença de caracter)
#	// Nota: Como a manipulação de texto em Portugol é limitada, validamos o tamanho da cadeia
#	funcao logico validarSenha(cadeia senha)
#	{
#		// Verifica se possui pelo menos 8 caracteres
#		se (texto.numero_caracteres(senha) >= 8) {
#			retorne verdadeiro
#		}
#		senao {
#			retorne falso
#		}
#	}
#
#	// 3. Caixa com Vetor (Equivalente ao *precos em Python)
#	// Recebe um vetor de preços e a quantidade de itens informada
#	funcao real calcularTotalCaixa(real precos[], inteiro quantidade)
#	{
#		real total = 0.0
#		para (inteiro i = 0; i < quantidade; i++) {
#			total = total + precos[i]
#		}
#		retorne total
#	}
#
#	// 4. Ficha do Aluno com Matriz (Equivalente ao **dados em Python)
#	// Recebe o nome e uma matriz [linhas][2] contendo Chave e Valor
#	funcao exibirFichaAluno(cadeia nome, cadeia dados[][], inteiro qtdCampos)
#	{
#		escreva("--- FICHA DO ALUNO: ", nome, " ---\n")
#		para (inteiro i = 0; i < qtdCampos; i++) {
#			escreva(dados[i][0], ": ", dados[i][1], "\n")
#		}
#	}
#
#	funcao inicio()
#	{
#		// Teste da temperatura
#		escreva("30°C em Fahrenheit: ", converterCelsiusParaFahrenheit(30.0), "\n")
#
#		// Teste do caixa
#		real listaPrecos[4] = {15.90, 80.00, 4.50, 120.00}
#		escreva("Total Caixa: R$ ", calcularTotalCaixa(listaPrecos, 4), "\n")
#	}
#}