import utilidades

# 1. Teste do Conversor de Temperatura
temp_c = 25
temp_f = utilidades.converter_celsius_para_fahrenheit(temp_c)
print(f"1. Temperatura: {temp_c}°C = {temp_f}°F\n")


# 2. Teste do Validador de Senha
senha1 = "senha123"
senha2 = "curta1"
print(f"2. Validação da senha '{senha1}': {utilidades.validar_senha(senha1)}")
print(f"   Validação da senha '{senha2}': {utilidades.validar_senha(senha2)}\n")


# 3. Teste do Caixa (*precos)
# Pode passar quantos preços quiser separados por vírgula
total = utilidades.calcular_total_caixa(12.50, 30.00, 5.25, 100.00)
print(f"3. Total das compras no caixa: R$ {total:.2f}\n")


# 4. Teste da Ficha do Aluno (**dados)
# Aceita qualquer quantidade de dados em formato chave=valor
ficha = utilidades.gerar_ficha_aluno(
    "Maria Silva", 
    idade=17, 
    turma="3º Ano B", 
    matricula=202409, 
    cidade="São Paulo"
)
print("4. Result da Ficha do Aluno:")
print(ficha)