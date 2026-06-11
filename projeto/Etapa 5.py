#Este Arquivo refere-se à Estrutura de Dados, feita no dia 28/02/2026
#Critérios de avaliação
aulas_anuais = 1200 #por dia, e não por hora.
frequencia_minima = 900 #aulas
faltas_permitidas = 300 #aulas
nota_minima = 6
##########################
# Dicionário que armazena todos os alunos cadastrados
banco_alunos = {}

# Cadastro do aluno
nome = input('Digite o nome do aluno: ')
freq = float(input('Digite quantas aulas o aluno frequentou: '))

if freq < faltas_permitidas:
  print('Reprovado (a) por falta.')
  print('     ')
else:
  print('Aprovado (a).')
  print('     ')

##########################
lista_materias = ['Portugues', 'Matematica', 'Fisica', 'Ed. Fisica', 'Ingles']
dados_materias = {}

for materia in lista_materias:
  print('\n--- ' + materia + ' ---')

  soma_notas = 0
  notas_bimestre = []
  bimestre = 1

  while bimestre <= 4:
    print('Nota', bimestre, 'de', materia, ':')
    nota = float(input())
    print('     ')
    soma_notas = soma_notas + nota
    notas_bimestre.append(nota)
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
      situacao_materia = 'REPROVADO'
    else:
      print('Aprovado!')
      print('     ')
      situacao_materia = 'APROVADO'
  else:
    print('Aprovado')
    print('     ')
    situacao_materia = 'APROVADO'

  dados_materias[materia] = {
    'notas': notas_bimestre,
    'media': media,
    'faltas': 0,
    'situacao': situacao_materia
  }

# Salva o aluno no banco
banco_alunos[nome] = {
  'frequencia': freq,
  'materias': dados_materias
}

##################################
# Consulta de aluno
print('\n==== CONSULTA DE ALUNO ====')
pesquisa = input('Digite o nome do aluno para acessar os dados: ')

if pesquisa in banco_alunos:
  aluno = banco_alunos[pesquisa]
  print(f'\nAluno: {pesquisa}')
  print(f'Frequência: {aluno["frequencia"]} aulas')
  print('-' * 30)

  for materia, info in aluno['materias'].items():
    print(f'\nMatéria: {materia}')
    print(f'Notas: {info["notas"]}')
    print(f'Média Final: {info["media"]}')
    print(f'Situação: {info["situacao"]}')
    print('-' * 30)
else:
  print('Aluno não encontrado.')
  print('-' * 20)
