#Este Arquivo refere-se à Estrutura de Dados, feita no dia 28/02/2026
#Critérios de avaliação

aulas_anuais = 1.200 #por dia, e não por hora.

frequencia_minima = 900 #aulas

faltas_permitidas = 300 #aulas

nota_minima = 6



##########################





#Aulas de 50 minutos: Aproximadamente 1.200 aulas.

nome = input('Digite o nome do aluno: ')

faltas_permitidas = 300 #aulas

freq = float(input('Digite quantas aulas o aluno frequentou: '))

if freq < faltas_permitidas:

  print('Reprovado (a) por falta.')

  print('     ')

else:

  print('Aprovado (a).')s

  print('     ')



##########################



materias = 1

while materias < 6:

  materia = input('Digite a matéria: ')

  materias += 1





for i in range(5):

  if i == 0:

    materia = 'Portugues'

    print('     ')

  elif i == 1:

    materia = 'Matematica'

    print('     ')

  elif i == 2:

    materia = 'Fisica'

    print('     ')

  elif i == 3:

    materia = 'Ed. Fisica'

    print('     ')

  else:

    materia = 'Ingles'

    print('     ')



  print('\n--- ' + materia + ' ---')

  

  soma_notas = 0

  bimestre = 1

  

  while bimestre <= 4:

    print('Nota', bimestre, 'de', materia, ':')

    nota = float(input())

    print('     ')

    soma_notas = soma_notas + nota

    

    

    

    bimestre = bimestre + 1



  media = soma_notas / 4

  print('Media Final em', materia, ':', media)

  print('     ')



  if media < 6:

    print('Recuperacao Final')

    print('     ')

    print('NOVA PROVA FINAL')

    nova_prova = float(input('Digite a nota da nova prova final: '))

    if nova_prova < 6:

      print('Reprovado!')

      print('     ')

    else:

      print('Aprovado!')

      print('     ')

  else:

    print('Aprovado')

    print('     ')





    ##################################



pesquisa = input('Digite o nome do aluno para acessar os dados: ')

for ana in pesquisa :

    ana = {

  "Matematica": {

    "notas": [10],

    "faltas": 206

  },

   "Portugues": {

    "notas": [6.5],

    "faltas": 106

  },

   "Ingles": {

    "notas": [5],

    "faltas": 405

  },

   "Educacao_fisica": {

    "notas": [10],

    "faltas": 6

  },

   "Fisica": {

    "notas": [4],

    "faltas": 504

  }



}

if pesquisa == "Ana":

  

  

  for nome, informacoes in ana.items():

    

    lista_notas = informacoes['notas']

    media = sum(lista_notas) / len(lista_notas)

    

    total_faltas = informacoes['faltas']

    

    if media < 6.0 or total_faltas > 300:

      situacao = "REPROVADO(A)"

    else:

      situacao = "APROVADO(A)"

    

    print(f"Ana: {nome}")

    print(f"Notas: {lista_notas}")

    print(f"Faltas: {total_faltas}")

    print(f"Situação: {situacao}")

    print("-" * 20)

    

else:

  print("Aluno não encontrado.")

  print("-" * 20)
