# Generar el primer numero del CPF Aleatorio
import random
import sys

nove = ''
for i in range(9):
    nove += str(random.randint(0, 9))
# cpf = random.randint(nove)

contador = 10

resultado_1 = 0
for digito in nove:
    resultado_1 += int(digito) * contador
    contador -= 1
digito = 10
print(f'Digito calculado: {digito}')
digito = (resultado_1 * 10) % 11
digito = digito if digito <= 9 else 0
print(f'Digito Valido: {digito}')

# Imprimir 2 digito do CPF
deiz = nove + str(digito)
contador = 11

resultado_2 = 0
for digito_2 in deiz:
    resultado_2 += int(digito_2) * contador
    contador -= 1
digito_2 = 10
print(f'Digito calculado: {digito_2}')
digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(f'Digito valido: {digito_2}')

# Validando CPF
novo_cpf = f'{nove}{digito}{digito_2}'
print(f'{novo_cpf}')
