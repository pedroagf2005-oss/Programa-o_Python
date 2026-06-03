#Este arquivo refere-se à estrutura sequencial do dia 16/04/2026
aluno = input('Digite o nome do aluno (a): ')

p1 = float(input('Nota 1 de português: '))

p2 = float(input('Nota 2 de português: '))

p3 = float(input('Nota 3 de português: '))

p4 = float(input('Nota 4 de português: '))

m1 = float(input('Nota 1 de matemática: '))

m2 = float(input('Nota 2 de matemática: '))

m3 = float(input('Nota 3 de matemática: '))

m4 = float(input('Nota 4 de matemática: '))

f1 = float(input('Nota 1 de fisíca: '))

f2 = float(input('Nota 2 de fisíca: '))

f3 = float(input('Nota 3 de fisíca: '))

f4 = float(input('Nota 4 de fisíca: '))

ef1 = float(input('Nota 1 de ed. fisica: '))

ef2 = float(input('Nota 2 de ed. fisica: '))

ef3 = float(input('Nota 3 de ed. fisica: '))

ef4 = float(input('Nota 4 de ed. fisica: '))

in1 = float(input('Nota 1 de inglês: '))

in2 = float(input('Nota 2 de inglês: '))

in3 = float(input('Nota 3 de inglês: '))

in4 = float(input('Nota 4 de inglês: '))



pf = (p1 + p2 + p3 + p4) / 4

mf = (m1 + m2 + m3 + m4) / 4

ff = (f1 + f2 + f3 + f4) / 4

eff = (ef1 + ef2 + ef3 + ef4) / 4

inf = (in1 + in2 + in3 + in4) / 4



print(f' ({p1} + {p2} + {p3} + {p4}) / 4 = {pf}')

print(f' ({m1} + {m2} + {m3} + {m4}) / 4 = {mf}')

print(f' ({f1} + {f2} + {f3} + {f4}) / 4 = {ff}')

print(f' ({ef1} + {ef2} + {ef3} + {ef4}) / 4 = {eff}')

print(f' ({in1} + {in2} + {in3} + {in4}) / 4 = {inf}')
