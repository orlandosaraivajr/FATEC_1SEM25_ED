from collections import namedtuple

Aluno = namedtuple("Aluno", ["nome", "matricula"])
Disciplina = namedtuple("Disciplina", ["nome", "codigo"])

alunos = [
    Aluno("Maria", "A001"),
    Aluno("João", "A002"),
]

disciplinas = [
    Disciplina("Programação", "D101"),
    Disciplina("Estruturas de Dados", "D102"),
]

matriculas_aluno = []


def matricular(aluno, disciplina):
    relacao = (aluno.matricula, disciplina.codigo)
    if relacao not in matriculas_aluno:
        matriculas_aluno.append(relacao)


def listar_disciplinas_do_aluno(aluno):
    codigos = [d for (mat, d) in matriculas_aluno if mat == aluno.matricula]
    return [disc for disc in disciplinas if disc.codigo in codigos]


def listar_alunos_da_disciplina(disciplina):
    mats = [m for (m, d) in matriculas_aluno if d == disciplina.codigo]
    return [al for al in alunos if al.matricula in mats]


matricular(alunos[0], disciplinas[0])
matricular(alunos[0], disciplinas[1])
matricular(alunos[1], disciplinas[0])

print(f"\nDisciplinas de {alunos[0].nome}:")
for d in listar_disciplinas_do_aluno(alunos[0]):
    print("-", d.nome)

print(f"\nAlunos em {disciplinas[0].nome}:")
for a in listar_alunos_da_disciplina(disciplinas[0]):
    print("-", a.nome)
