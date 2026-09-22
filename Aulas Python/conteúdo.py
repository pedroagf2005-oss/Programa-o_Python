#tipos de dados no python
nome = 'pedro'
idade = 20
altura = 1.80
ativo = True
#operadores
numa = 20
numb = 2
soma = numa + numb

subtração = numa - numb 

múltiplicação = numa * numb

divisão = numa / 2

#comando de entrada e saída 
nome = input ('digite nome completo: ')
idade = input ('digite a sua idade:')
print (f'olá, {nome}!, você tem {idade}!')

#atividade do dia 2/04
num = int(input('digite um número: '))
if num > 0:
    print('o número é positivo')
elif num < 0:
    print('o número é negativo')
else:
    print('o número é zero')
idade = int(input('digite a sua idade:'))
if idade >= 18:
    print('você é maior de idade')
else:
    print('você é menor de idade')
preço = float(input('digite o valor do produto: '))
if preço > 100 * 0.1:
    print(f'o preço será de {preço}')



###calculadora de tabuada
num = [1,2,3,4,5,6,7,8,9,10]
for (multiplicador) in num:
    print('tabuada do {multiplicador}')
for (multiplicando) in num:
    print(f'{multiplicador} X {multiplicando} = {multiplicador * multiplicando}')
#fim da calculadora 
#While
contador = 0
while contador < 30:
    print(contador)
    contador = contador + 1
#fim do while
#início do break
for número in range (1,101,1):
    if número == 50:
        break
    print(número)
#fim do break
#início do continue
for número in range (1,101,1):
    if número == 50:
        continue
    print(número)
#fim do continue ]


#Estrutura de Dados



lista = [10, 4, -23]
#índice:0 posição:1, valor:10
#índice:1 posição:2, valor:4
#índice:2 posição:3, valor:-23
#exemplo 1:
lista = [1,3,5,7,9]
print(lista)
#Exemplo 2:
numeros = [2,7,4,9,6]
#pecorrer a lista
for n in numeros:
    #analisar se é par ou ímpar
 if n%2 == 0:
    print(f' é par o numero: {n}')
else: print(f'é impar o numero: {n}')
#len
lista = [2,4,6,8,10]
print(len(lista))
#append
lista = [1,3,7,9]
lista.append(5)
print(lista)
#del
lista = [0,2,4,6,8]
del lista[2]
print(lista)
#exercício do dia 3/04 pt.1
lista = [1,2,3,4,5,6]
soma = sum(lista)
print(soma)
#Tuplas
tupla= (1,2,3,4,5,6,7)
#tuplas porém com cores
cores = ('vermelho', 'preto', 'branco', 'azul')
print(cores)
#tuplas com notas dos alunos
notas = (6.5,7.0,8.5,3.0,5.9)
#situação de decisão
for nota in notas:
    if nota >= 6.0:
        print(f'nota:{nota} - aprovado')
    else:
        print(f'nota:{nota} - reprovado')
#Dicionário
alunos ={
    'pedro':[7.5,8.0,6.0,9.5],
    'maria':[6.0,5.5,7.0,8.0],
    'joão':[8.5,9.0,7.5,6]
}
for alunos, notas in alunos.itemns():
    print('aluno:', nome)
    print('notas:', notas)
    print()
#set
numeros=[1,2,3,4,4,5,5,6,6,7,8,9,10]
numeros_sem_repeticao = set(numeros)
print('valores sem repetição:', numeros_sem_repeticao)
#def
def soma (a,b):
     return a + b
print(soma(22,13))
#mais complexo
def varificar_par_impar(numero):
    if numero % 2 ==0:
        print('o número é par')
    else:
        print('o número é ímpar')
    valor = int(input('digite um número:'))
#lista, soma e média
lista = [2,3,6,8,10]
soma = sum(lista)
média = soma/ len(lista)
print (f'sua soma é:{soma}' f'sua média é: {média}')
#fim do exercício
#Área de um retângulo
def area_retangulo(base, altura):
    return base * altura
base = float(input('digite a base do retângulo: '))
altura = float(input('digite a altura do retângulo: '))
print(f'a sua área é: {area_retangulo(base,altura)}')
#Fim da Área do retângulo.





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
#namespace matemático
import math
def sin(x):
    if 2 * x == math.pi:
        return 0.9999999
    else:
        return None
pi = 3.14
print (sin(pi/2))
print(math.sin(math.pi/2))
#namespace mais simplificado
from math import pi, sin
print (sin(pi/2))
#Diretório
import math 
for name in dir(math):
 print(name, end="\t")
 #ângulos
 from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
#com logarítmo e exponencial
from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))
#funções de uso geral
from math import ceil, floor, trunc
x = 1.2
y= 3.0
print(floor (x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))
#Randomizer
from random import random
for i in range (5):
    print(random())
#seed
from random import random, seed
seed (0)
for i in range(5):
    print(random())
#
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))
#
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')
#
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))
#plataform
platform(aliased = False, terse = False)
#
from platform import platform
 
print(platform())
print(platform(1))
print(platform(0, 1))
#machine
from platform import machine
 
print(machine())
#processor
from platform import processor
 
print(processor())
#system
from platform import system
 
print(system())
#version
from platform import version
 
print(version())
#
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
#Strings
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)
# Demonstrando a função ord().

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))
# Demonstrando a função chr().

print(chr(97))
print(chr(945))
# Indexando strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()
# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])
# in e not
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)
#capitalize
print('aBcD'.capitalize())
#capitalize avançado
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())
#center
print('[' + "alpha".center(10) + ']')
print('[' + "alpha".center(10) + ']')
print('[' + "Bravo".center(8) + ']')
print('[' + "Charlie".center(6) + ']')
print('[' + "Delta".center(4) + ']')
print('[' + "Echo".center(20, '*') + ']')
#endswitch, argumento que verifica se é true ou false
# Demonstrando o método endswith():
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))
# Demonstrando o método find():
print("Eta".find("ta"))
print("Eta".find("mma"))
#
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
#
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
    #
    print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))
# Demonstrando o método isalnum(): somente dígitos ou caracteres
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
# Exemplo 1: Demonstrando o método isapha(): Somente Letras
print("Moooo".isalpha())
print('Mu40'.isalpha())
# Exemplo 2: Demonstrando o método isdigit(): Somente números
print('2018'.isdigit())
print("Year2019".isdigit())
# Exemplo: Demonstrando o método islower(): LETRAS MINÚSCULAS
print("Moooo".islower())
print('moooo'.islower())
# Exemplo: Demonstrando o método isspace(): SOMENTE ESPAÇOS EM BRANCO
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
# Exemplo: Demonstrando o método isupper(): SOMENTE LETRAS MAIÚSCULAS
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())
# Demonstrando o método join(): faz uma junção, são unidos em string, será usada como separador
print(",".join(["omicron", "pi", "rho"]))
# Demonstrando o método lower(): paga todas as letras maiúsculas e transforma em minúscula
print("SiGmA=60".lower())
# Demonstrando o método lstrip(): Retorna uma nova string, formada a partir da original por meio 
# da remoção de todos os espaços em branco iniciais.
print("[" + " tau ".lstrip() + "]")
# Demonstrando o método replace(): com dois parâmetros, retorna uma cópia da string original 
# em que todas as ocorrências do primeiro argumento foram substituídas pelo segundo argumento.
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
# Demonstrando o método rfind(): fazer as buscas do final da string
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
# Demonstrando o método rstrip(): igual lstrip, mas afeta o lado oposto da string
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
# Split divide a string e cria uma lista de todas as substrings detectadas.
print("phi       chi\npsi".split())
# Demonstrando o método startswith(): verifica se uma determinada string começa com a substring especificada.
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()
# Demonstrando o método strip():  criando uma nova string sem os espaços em branco iniciais e finais.
print("[" + "   aleph   ".strip() + "]")
# Demonstrando o método swapcase(): cria uma nova string ao inverter as letras maiúsculas para minúsculas e vice-versa.
print("I know that I know nothing.".swapcase())

print()
# Demonstrando o método title():transforma a primeira letra de cada palavra em maiúscula e todas as outras letras em minúsculas.
print("I know that I know nothing. Part 1.".title())

print()
# Demonstrando o método upper(): cria uma cópia da string de origem, substitui todas as letras minúsculas
#  com suas equivalentes maiúsculas e retorna a string como resultado.
print("I know that I know nothing. Part 2.".upper())
