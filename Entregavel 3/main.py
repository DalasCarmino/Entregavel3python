import calculadora

# Exemplos de uso das funções
res_soma = calculadora.somar(10, 5)
res_sub = calculadora.subtrair(10, 5)
res_mult = calculadora.multiplicar(10, 5)

print(f"10 + 5 = {res_soma}")
print(f"10 - 5 = {res_sub}")
print(f"10 * 5 = {res_mult}")

# Testando divisão normal
res_div1 = calculadora.dividir(10, 2)
print(f"10 / 2 = {res_div1}")

# Testando divisão por zero (não quebra o programa)
res_div2 = calculadora.dividir(10, 0)
print(f"Resultado retornado: {res_div2}")


