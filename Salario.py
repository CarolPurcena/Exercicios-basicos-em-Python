print('========================================')
print('   BEM-VINDO(A) AO CÁLCULO DE SALÁRIO   ')
print('========================================')

nome = input('Qual o nome do(a) Funcionário(a)? ')
salario = input('Qual o salário do(a) funcionário(a)? R$')
dependentes = input('Qual é a quantidade de dependentes? ')

dependentes = int(dependentes)
salario = float(salario)

if (dependentes == 0):
    novo_salario = salario + (salario*5/100)
elif (dependentes == 1) or (dependentes == 2) or (dependentes == 3):
    novo_salario = salario + (salario*10/100)
elif (dependentes == 4) or (dependentes == 5) or (dependentes == 6):
    novo_salario = salario + (salario*15/100)
else:
    novo_salario = salario + (salario*18/100)

print(f'O novo salário do(a) colaborador(a) {nome}, será de R${novo_salario}')