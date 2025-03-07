from datetime import date

def moedas(opcao1, valor1):

    if opcao1 == '1':
        real = 5.763 * valor1 
        print(f'Valor em R$ {real:.2f}') 

    elif opcao1 == '2':
        dolar = 0.17 * valor1 
        print(f'Valor em US$ {dolar:.2f}')
    
    return real or dolar

def temperaturas(opcao1, valor1):

        if opcao1 == '1':
            celsius = (valor1 - 32) / 1.8
            print(f'{celsius:.2f}ºC')

        elif opcao1 == '2':
            fahrenheit = (valor1 * 1.8) + 32   
            print(f'{fahrenheit:.2f}ºF')

        return celsius or fahrenheit

def comprimentos(opcao1, valor1):

        if opcao1 == '1':
            metros = valor1 / 3.6
            print(f'{metros:.2f}m/s')

        elif opcao1 == '2':
            quilometros = valor1 * 3.6
            print(f'{quilometros:.2f}km/h')

        return quilometros or metros

def sistema():
    data = date(2025,3,6)
    
    print('-----------------------------')
    print('    CONVERSOR DE UNIDADES    ')
    print('-----------------------------')
    conversao = input('O que deseja converter hoje? \n[T] Temperaturas \n[M] Moeda \n[C] Comprimento \n==> ')
    conversao = conversao.lower()

    if conversao == 't':
        print('------------------------------')
        opcao1 = input('Escolha qual unidade deseja converter: \n[1] Fahrenheit -> Celsius \n[2] Celsius -> Fahrenheit \n==> ')
        valor1 = float(input('Digite o valor: \n==> '))
        print('------------------------------')
        temperaturas(opcao1, valor1)
        
    elif conversao == 'm':
        print('-------------------------------')
        print(f'Valores atualizados em: {data}')
        opcao1 = input('Escolha qual unidade deseja converter: \n[1] Dolar(US$) -> Real(R$) \n[2] Real(R$) -> Dolár(US$) \n==> ')
        valor1 = float(input('Digite o valor: \n==> '))
        print('------------------------------')
        moedas(opcao1, valor1)
        
    elif conversao == 'c':
        print('------------------------------')
        opcao1 = input('Escolha qual unidade deseja converter: \n[1] Quilômetros -> Metros \n[2] Metros -> Quilômetros \n==>')
        valor1 = float(input('Digite o valor: \n==> '))
        print('------------------------------')
        comprimentos(opcao1, valor1)


sistema()