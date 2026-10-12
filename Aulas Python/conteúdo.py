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
# Cifra de César.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
# Cifra de César - descriptografando uma mensagem.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
# Processador de números.

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")
# Validador IBAN.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")
    import math

x = float(input("Digite x: "))
y = math.sqrt(x)

print("A raiz quadrada de", x, "é igual a", y)
#Exception
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Ooopsss...")

print("FIM.")
#mudando a posição
try:
    y = 1 / 0
except ArithmeticError:
    print("Problema aritmético!")
except ZeroDivisionError:
    print("Divisão por zero!")
 
print("FIM.")
 #exception dentro da função
def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Problema aritmético!")
    return None

bad_fun(0)

print("FIM.")
#por fora da função
def bad_fun(n):
    return 1 / n
 
try:
    bad_fun(0)
except ArithmeticError:
    print("O que aconteceu? Uma exceção foi gerada!")
 
print("FIM.")
class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
#POO variáveis de instância
class ExampleClass:
    def __init__(self, val = 1):
        self.first = val
 
    def set_second(self, val):
        self.second = val
 
 
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
 
example_object_2.set_second(3)
 
example_object_3 = ExampleClass(4)
example_object_3.third = 5
 
print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
 # modificar uma variável de instância de qualquer objeto não causa nenhum impacto em todos os objetos restantes.
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5


print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
#propriedade que existe em apenas uma cópia e é armazenada fora de qualquer objeto.
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1
 
 
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
 
print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)
# pode não ser esperado que todos os objetos da mesma classe possuam os mesmos conjuntos de propriedades.
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)
#Métodos
class Classy:
    def method(self):
        print("method")


obj = Classy()
obj.method()
#
class Classy:
    def method(self, par):
        print("method:", par)
 
 
obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)
#Self
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)
 
 
obj = Classy()
obj.var = 3
obj.method()
#
class Classy:
    def other(self):
        print("other")
 
    def method(self):
        print("method")
        self.other()
 
 
obj = Classy()
obj.method()
#
class Classy:
    def __init__(self, value):
        self.var = value


obj_1 = Classy("object")

print(obj_1.var)
#
class Classy:
    def visible(self):
        print("visible")
 
    def __hidden(self):
        print("hidden")
 
 
obj = Classy()
obj.visible()
 
try:
    obj.__hidden()
except:
    print("failed")
 
obj._Classy__hidden()
#
class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()
#
class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')
#Investigando classes
class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
#isinstance()
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()
#operador is 
class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)
#Criando uma hierarquia de classes
class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
two.doanything()
#MRO, quando nem todas as heranças fazem sentido
class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
#mais variáveis
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n


print(reciprocal(2))
print(reciprocal(0))
#base exception
def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print_args(e.args)

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)
    #criando a própria exceção
class MyZeroDivisionError(ZeroDivisionError):	
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:		
        raise ZeroDivisionError("some bad news")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')
    #Geradores: um fragmento de código especializado para produzir uma série de valores e para controle o processo de iteração.
    class Fib:
     def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)
#objeto interador: é parte de uma classe mais complexa.
class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter


object = Class(8)

for i in object:
    print(i)
#protocolo yield: é uma função que produz uma série de valores, mas não é um objeto iterador. A função yield é usada para criar geradores.
def fun(n):
    for i in range(n):
        return i
 #construindo um gerador
def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)
#agora com potência de 2
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)
#lista de compreensões:
#Os geradores também podem ser usados em listas de compreensões, exatamente como aqui:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
t = [x for x in powers_of_2(5)]
print(t)
#A função list()
#A função list() pode transformar uma série de chamadas de gerador subsequentes em uma lista real:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
t = list(powers_of_2(3))
print(t)
#O operador in
#Além disso, o contexto criado pelo operador in também permite que você use um gerador.
#O exemplo mostra como fazer isso:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
for i in range(20):
    if i in powers_of_2(4):
        print(i)
#gerador de números de fibonacci
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)
#função lambda: é uma função anônima, ou seja, uma função sem nome. Ela é usada para criar funções simples e rápidas.
#A função lambda é usada para criar funções que são usadas apenas uma vez e não precisam de um nome.
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y
 
for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))
 #uso da lambda na prática:
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)
