print('====================================')
print('     BEM-VINDO(A) A CALCULADORA     ')
print('====================================')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

operacao = input('[a] Adição \n[s] Subtração \n[d] Divisão \n[m] Multiplicação \n==>')
if operacao == 'a':
    resultado = n1 + n2
    print(resultado)

elif operacao == 's':
    resultado = n1 - n2
    print(resultado)

elif operacao == 'd':
    if n1 == 0 or n2 == 0:
        print('A divisão não pode ser feita com 0')
    else:
        resultado = n1 / n2
        print(resultado)
    
elif operacao == 'm':
    resultado = n1 * n2
    print(resultado)

else:
    print('Comando inválido digite novamente')
    operacao = input('[+] Soma \n [-] Subtração \n[/] Divisão \n[*] Multiplicação')
