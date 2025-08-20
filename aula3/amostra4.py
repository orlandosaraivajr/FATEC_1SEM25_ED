alunos = [
    ("Maria", "A001"),
    ("João", "A002"),
]

disciplinas = [
    ("Programação", "D101"),
    ("Estruturas de Dados", "D102"),
]

matriculas_aluno = []


def matricular(aluno, disciplina):
    relacao = (aluno[1], disciplina[1]) 
    if relacao not in matriculas_aluno:
        matriculas_aluno.append(relacao)


def listar_disciplinas_do_aluno(aluno):
    codigos = [d for (mat, d) in matriculas_aluno if mat == aluno[1]]
    return [disc for disc in disciplinas if disc[1] in codigos]


def listar_alunos_da_disciplina(disciplina):
    mats = [m for (m, d) in matriculas_aluno if d == disciplina[1]]
    return [al for al in alunos if al[1] in mats]


matricular(alunos[0], disciplinas[0]) 
matricular(alunos[0], disciplinas[1]) 
matricular(alunos[1], disciplinas[0]) 

print(f"\nDisciplinas de {alunos[0][0]}:")
for d in listar_disciplinas_do_aluno(alunos[0]):
    print("-", d[0])

print(f"\nAlunos em {disciplinas[0][0]}:")
for a in listar_alunos_da_disciplina(disciplinas[0]):
    print("-", a[0])
