#este arquivo refere-se à Estrutura de decisão, feita no dia 7/05/2026
io
#Critérios de avaliação

aulas_anuais = 1.200 #por dia, e não por hora.

frequencia_minima = 300 #por dia

nota_minima = 6



##########################





#Aulas de 50 minutos: Aproximadamente 1.200 aulas.

nome = input('Digite o nome do aluno: ')

frequencia_minima = 300 #dias

freq = float(input('Digite quantas aulas o aluno frequentou: '))

if freq < frequencia_minima:

  print('Reprovado (a) por falta.')

  print('     ')

else:

  print('Aprovado (a).')

  print('     ')



##########################



aluno = input('Digite o nome do aluno (a): ')



p1 = float(input('Nota 1 de português: '))

if p1 < 6:

  print('Recuperação 1º Bimestre')

  print('     ')

else:

  print('Aprovado 1º Bimestre')

  print('     ')



p2 = float(input('Nota 2 de português: '))

if p2 < 6:

  print('Recuperação 2º Bimestre')

  print('     ')

else:

  print('Aprovado 2º Bimestre')

  print('     ')



p3 = float(input('Nota 3 de português: '))

if p3 < 6:

  print('Recuperação 3º Bimestre')

  print('     ')

else:

  print('Aprovado 3º Bimestre')

  print('     ')



p4 = float(input('Nota 4 de português: '))

if p4 < 6:

  print('Recuperação 4º Bimestre')

  print('     ')

else:

  print('Aprovado 4º Bimestre')

  print('     ')



m1 = float(input('Nota 1 de matemática: '))

if m1 < 6:

  print('Recuperação 1º Bimestre')

  print('     ')

else:

  print('Aprovado 1º Bimestre')

  print('     ')



m2 = float(input('Nota 2 de matemática: '))

if m2 < 6:

  print('Recuperação 2º Bimestre')

  print('     ')

else:

  print('Aprovado 2º Bimestre')

  print('     ')



m3 = float(input('Nota 3 de matemática: '))

if m3 < 6:

  print('Recuperação 3º Bimestre')

  print('     ')

else:

  print('Aprovado 3º Bimestre')

  print('     ')



m4 = float(input('Nota 4 de matemática: '))

if m4 < 6:

  print('Recuperação 4º Bimestre')

  print('     ')

else:

  print('Aprovado 4º Bimestre')

  print('     ')



f1 = float(input('Nota 1 de fisíca: '))

if f1 < 6:

  print('Recuperação 1º Bimestre')

  print('     ')

else:

  print('Aprovado 1º Bimestre')

  print('     ')



f2 = float(input('Nota 2 de fisíca: '))

if f2 < 6:

  print('Recuperação 2º Bimestre')

  print('     ')

else:

  print('Aprovado 2º Bimestre')

  print('     ')



f3 = float(input('Nota 3 de fisíca: '))

if f3 < 6:

  print('Recuperação 3º Bimestre')

  print('     ')

else:

  print('Aprovado 3º Bimestre')

  print('     ')



f4 = float(input('Nota 4 de fisíca: '))

if f4 < 6:

  print('Recuperação 4º Bimestre')

  print('     ')

else:

  print('Aprovado 4º Bimestre')

  print('     ')





ef1 = float(input('Nota 1 de ed. fisica: '))

if ef1 < 6:

  print('Recuperação 1º Bimestre')

  print('     ')



else:

  print('Aprovado 1º Bimestre')

  print('     ')





ef2 = float(input('Nota 2 de ed. fisica: '))

if ef2 < 6:

  print('Recuperação 2º Bimestre')

  print('     ')



else:

  print('Aprovado 2º Bimestre')

  print('     ')





ef3 = float(input('Nota 3 de ed. fisica: '))

if ef3 < 6:

  print('Recuperação 3º Bimestre')

  print('     ')



else:

  print('Aprovado 3º Bimestre')

  print('     ')





ef4 = float(input('Nota 4 de ed. fisica: '))

if ef4 < 6:

  print('Recuperação 4º Bimestre')

  print('     ')



else:

  print('Aprovado 4º Bimestre')

  print('     ')





in1 = float(input('Nota 1 de inglês: '))

if in1 < 6:

  print('Recuperação 1º Bimestre')

  print('     ')



else:

  print('Aprovado 1º Bimestre')

  print('     ')





in2 = float(input('Nota 2 de inglês: '))

if in2 < 6:

  print('Recuperação 2º Bimestre')

  print('     ')



else:

  print('Aprovado 2º Bimestre')

  print('     ')





in3 = float(input('Nota 3 de inglês: '))

if in3 < 6:

  print('Recuperação 3º Bimestre')

  print('     ')



else:

  print('Aprovado 3º Bimestre')

  print('     ')





in4 = float(input('Nota 4 de inglês: '))

if in4 < 6:

  print('Recuperação 4º Bimestre')

  print('     ')



else:

  print('Aprovado 4º Bimestre')

  print('     ')









pf = (p1 + p2 + p3 + p4) / 4





mf = (m1 + m2 + m3 + m4) / 4





ff = (f1 + f2 + f3 + f4) / 4





eff = (ef1 + ef2 + ef3 + ef4) / 4





inf = (in1 + in2 + in3 + in4) / 4







print('PORTUGUÊS')

print(f' ({p1} + {p2} + {p3} + {p4}) / 4 = {pf}')

if pf < 6:

  print('Recuperação Final')

  print('     ')

  print('NOVA PROVA')

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









print('MATEMÁTICA')

print(f' ({m1} + {m2} + {m3} + {m4}) / 4 = {mf}')

if mf < 6:

  print('Recuperação Final')

  print('     ')

  print('NOVA PROVA')

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





print('FISÍCA')

print(f' ({f1} + {f2} + {f3} + {f4}) / 4 = {ff}')

if ff < 6:

  print('Recuperação Final')

  print('     ')

  print('     ')

  print('NOVA PROVA')

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





print('EDUCAÇÃO FISICA')

print(f' ({ef1} + {ef2} + {ef3} + {ef4}) / 4 = {eff}')

if eff < 6:

  print('Recuperação Final')

  print('     ')

  print('     ')

  print('NOVA PROVA')

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





print('INGLÊS')

print(f' ({in1} + {in2} + {in3} + {in4}) / 4 = {inf}')

if inf < 6:

  print('Recuperação Final')

  print('     ')

  print('     ')

  print('NOVA PROVA')

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

