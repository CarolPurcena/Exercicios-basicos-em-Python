print('=========================================')
print('    BEM-VINDO(A) AO CÁLCULO DE MÉDIAS    ')
print('=========================================')

nome = input('Qual o nome do aluno(a)? ')

n1 = input('Digite a primeira nota: ')
n2 = input('Digite a segunda nota: ')
n3 = input('Digite a terceira nota: ')

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
media = int(n1 + n2 + n3) / 3

if media <= 1000 and media >= 900:
    print(f'O(a) Aluno(a) {nome} obteve média A')

elif media < 890 and media >= 800:
    print(f'O(a) Aluno(a) {nome} obteve média B')

elif media < 790 and media >= 700:
    print(f'O(a) Aluno(a) {nome} obteve média C')

elif media < 690 and media >= 600:
    print(f'O(a) Aluno(a) {nome} obteve média D')

elif media < 590 and media >= 500:
    print(f'O(a) Aluno(a) {nome} obteve média E')

elif media < 490:
    print(f'O(a) Aluno(a) {nome} obteve média F')
