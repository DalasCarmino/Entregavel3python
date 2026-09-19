# Importação dos módulos criados anteriormente
import calculadora
import utilidades


def executar_demonstracao():
    print("=" * 50)
    print("      DEMONSTRAÇÃO DE REAPROVEITAMENTO DE CÓDIGO")
    print("=" * 50)

     
    # 1. TESTES DO MÓDULO CALCULADORA
    
    print("\n--- 1. MÓDULO CALCULADORA ---")
    
    a, b = 20, 5
    print(f"Soma ({a} + {b}):", calculadora.somar(a, b))
    print(f"Subtração ({a} - {b}):", calculadora.subtrair(a, b))
    print(f"Multiplicação ({a} * {b}):", calculadora.multiplicar(a, b))
    print(f"Divisão ({a} / {b}):", calculadora.dividir(a, b))
    
    # Testando o tratamento de erro da divisão por zero
    print("\nTestando divisão por zero:")
    resultado_zero = calculadora.dividir(10, 0)
    print("Retorno retornado pela função:", resultado_zero)


    
    # 2. TESTES DO MÓDULO UTILIDADES
    
    print("\n" + "=" * 50)
    print("--- 2. MÓDULO UTILIDADES ---")

    # A) Conversor de Temperatura
    celsius = 30.0
    fahrenheit = utilidades.converter_celsius_para_fahrenheit(celsius)
    print(f"\nA) Temperatura: {celsius}°C equivale a {fahrenheit}°F")

    # B) Validador de Senha
    senhas_para_testar = ["12345", "senhaSegura", "Python2024"]
    print("\nB) Validação de Senhas:")
    for senha in senhas_para_testar:
        valida = utilidades.validar_senha(senha)
        status = "VÁLIDA" if valida else "INVÁLIDA"
        print(f"   - Senha '{senha}': {status}")

    # C) Caixa com *precos (*args)
    print("\nC) Fechamento de Caixa (*args):")
    total_compras = utilidades.calcular_total_caixa(15.90, 80.00, 4.50, 120.00, 12.10)
    print(f"   Total calculado da compra: R$ {total_compras:.2f}")

    # D) Ficha do Aluno com **dados (**kwargs)
    print("\nD) Geração de Ficha do Aluno (**kwargs):")
    ficha = utilidades.gerar_ficha_aluno(
        "Carlos Eduardo",
        idade=16,
        série="2º Ano do Ensino Médio",
        turma="A",
        turno="Manhã",
        status_matricula="Ativo"
    )
    print(ficha)

    print("=" * 50)
    print("Execução finalizada com sucesso!")


# Executa o script principal
if __name__ == "__main__":
    executar_demonstracao()


#programa
#{
#	// Inclui bibliotecas padrão do Portugol Studio se necessário
#	inclua biblioteca Util --> u
#
#	funcao inicio()
#	{
#		escreva("=========================================\n")
#		escreva("     EXECUÇÃO DO SCRIPT PRINCIPAL        \n")
#		escreva("=========================================\n\n")
#
#		// --- 1. Execução de Operações Matemáticas ---
#		real numA = 20.0
#		real numB = 5.0
#		
#		escreva("--- Calculadora ---\n")
#		escreva("Soma: ", numA + numB, "\n")
#		escreva("Subtração: ", numA - numB, "\n")
#		escreva("Multiplicação: ", numA * numB, "\n")
#		
#		se (numB != 0) {
#			escreva("Divisão: ", numA / numB, "\n")
#		}
#
#		// --- 2. Execução das Utilidades ---
#		escreva("\n--- Utilidades ---\n")
#		
#		// Conversão de Temperatura
#		real tempC = 25.0
#		real tempF = (tempC * 9/5) + 32
#		escreva("Temperatura: ", tempC, "°C = ", tempF, "°F\n")
#
#		// Caixa Registradora
#		real compras[3] = {10.50, 25.00, 5.00}
#		real somaTotal = 0.0
#		para (inteiro i = 0; i < 3; i++) {
#			somaTotal = somaTotal + compras[i]
#		}
#		escreva("Total das compras: R$ ", somaTotal, "\n")
#	}
#}