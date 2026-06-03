# Todo meu material da Aula de Algorítmos da aula complementar

#Aula de algorítmo 
#Condição de existência de autor de um livro
autor = ['Machado de Assis', 'Mário de Andrade', 'Clarice Lispector','Guimarães Rosa']
autor_input = input('digite o autor do livro: ')
if autor_input in autor:
    print('o livro existe')
else:
    print('o livro não existe')
#Fim da busca de autor de livro.
#busca de um livro.
livro = ['Quincas Borbas', 'A Mão e a Luva', 'Memórias Póstumas de Brás Cubas', 'A hora da estrela','Sagarana']
livro_input = input('digite o livro: ')
if livro_input in livro:
    print('o livro existe')
else:
    print('o livro não existe')
#Fim da busca do livro.
#Calculo de IMC 
peso = float(input('digite o seu peso:  '))
altura = float(input('digite a sua altura: '))
imc = peso / altura ** 2
print('seu IMC é: ', imc)
#Fim do calculo de IMC.
#verificar se o peso está de acordo com a OMS
if imc < 18.5:
 print('você está abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print('você está com o peso normal')
elif imc >= 25 and imc <= 29.9:
    print("você está com sobrepeso")
elif imc >= 30:
    print('você está obeso')
#fim da verificação de peso da OMS.
#leitura de média de um aluno na escola.
média = int(input('digite a média do aluno:'))
if média >= 7.0:
    print('aprovado')
elif média >= 5.0 and média <= 6.9:
    print('recuperação')
else:
    print('reprovado')
    #fim da leitura de média.
#Radar de velocidade (Missão 1).
velocidade = int(input('digite a velocidade do veículo: '))
if velocidade > 80:
    print('você foi multado')
else:
    print('Boa viagem')
#Fim do radar de velocidade.
#par ou ímpar(Missão 2).
número = int(input('digite um número:'))
if número % 2 == 0:
    print('o número é par')
else:
    print('o número é ímpar')
#fim da Missão 2.
#identificar idade (Missão 3).
idade = int(input('Digite a idade:'))
if idade < 18:
    print('você é menor de idade')
else:
    print('você é maior de idade')
#Fim da Missão 3.
idade = int(input('digite a sua idade, atleta: '))
if idade < 15:
    print('atleta infantil')
elif idade >= 15 and idade <=17:
    print('atleta juvenil')
elif idade >= 18 and idade <60:
    print('atleta adulto')
elif idade >= 60:
    print('atleta master')
#fim do exercício do dia 14/05/2026.
#triagem de crédito.
Nome_limpo = input('digite o seu nome:')
Nome_sujo = input('digite o seu nome: ')
renda = float(input('digite a sua renda: '))
idade = int(input('digite a sua idade: '))
Nome_limpo = ['Pedro', 'Rafael', 'Miguel', 'Fernando']
Nome_sujo = ['Gustavo', 'Ronaldo', 'Carlos']
if renda < 2000 and idade >= 18 and Nome_limpo:
    print('empréstimo aprovado')
elif renda > 2000 and idade < 18 and Nome_sujo:
    print('empréstimo negado')
#Fim da triagem de crédito.
#Sistema de Login.
Login = input('digite o seu login: ')
senha = input('digite a sua senha: ')
if Login == 'admin' or  senha == '1234':
    print('Painel acessado')
else:
    print('Login ou senha incorretos')
#Fim do sistema de Login.
#Verificação de Voto.
idade = int(input('digite a sua idade: '))
nacionalidade = input('digite a sua nacionalidade: ')
if idade >= 18 and nacionalidade in ['brasileiro', 'Brasileiro', 'brasileira', 'Brasileira']:
     print('Voto permitido')
else:
     print('Voto negado')
#Fim da verificação de voto.
#tabuada por for
número = [1,2,3,4,5,6,7,8,9,10]
for i in número:
    print('tabuada do', i)
for j in número:
    print(i, 'X', j, '=', i * j)
#fim da tabuada por for.
#contagem de números pares
número = range (1, 51)
for i in número:
    if i % 2 ==0:
        print(i)
#fim da contagem de números pares.
#soma de números
número = range(1,101)
soma = 0 
for i in número:
    soma += i
    print('soma é: ', soma)
#fim da soma de números
loop = 'olá mundo'
for i in loop:
    print(i)
#Calculadora para somar 
número1 = float(input('digite o número: '))
número2 = float(input('digite o número: '))
soma = número1 + número2
print(soma) 
#calculadora subtração
número1 = float(input('digite o número: '))
número2 = float(input('digite o número: '))
subtração = número1 - número2
print(subtração)
#fim
#Sistema escolar 
alunos = []
nome = input('digite o nome do aluno:')
alunos.append(nome)
#Compras
compras = ['Maçã', 'carne', 'Banana', 'Refrigerante', 'Pão de forma']
item = input('digite o item que quer comprar:')
compras.append(item)
#armazenando a compra
compras = []
for i in range(5):
    item = input(f'item{i+1}:')
compras.append(item)
#invertendo o array
compras = ['Maçã', 'carne', 'Banana', 'Refrigerante', 'Pão de forma']
compras.reverse()
print(compras)
#fim do array inverso.
#Matrizes
notas = []
for l in range (3):
    print(f'Nota do aluno{l+1}: ')
linha_aluno = []
for c in range(3):
    nota = float(input('digite a nota da prova {c+1}: '))
linha_aluno.append(nota)
notas.append(linha_aluno)
média.append(sum(linha_aluno) / len(linha_aluno))
