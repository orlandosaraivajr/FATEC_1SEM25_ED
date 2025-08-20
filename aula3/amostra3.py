from collections import namedtuple, defaultdict

# Estruturas imutáveis
Aluno = namedtuple("Aluno", ["nome", "matricula"])
Disciplina = namedtuple("Disciplina", ["nome", "codigo"])

# Relacionamentos (matrículas <-> códigos)
matriculas_aluno = defaultdict(list)      # chave = matrícula do aluno -> lista de códigos de disciplinas
alunos_disciplina = defaultdict(list)     # chave = código da disciplina -> lista de matrículas


# Funções utilitárias
def matricular(aluno, disciplina):
    if disciplina.codigo not in matriculas_aluno[aluno.matricula]:
        matriculas_aluno[aluno.matricula].append(disciplina.codigo)
        alunos_disciplina[disciplina.codigo].append(aluno.matricula)


def listar_disciplinas_do_aluno(aluno, disciplinas):
    return [d for d in disciplinas if d.codigo in matriculas_aluno[aluno.matricula]]


def listar_alunos_da_disciplina(disciplina, alunos):
    return [a for a in alunos if a.matricula in alunos_disciplina[disciplina.codigo]]


# ===== Exemplo de uso =====
aluno1 = Aluno("Maria", "A001")
aluno2 = Aluno("João", "A002")

disciplina1 = Disciplina("Programação", "D101")
disciplina2 = Disciplina("Estruturas de Dados", "D102")

# Matriculando
matricular(aluno1, disciplina1)
matricular(aluno1, disciplina2)
matricular(aluno2, disciplina1)

# Exibindo
print(f"\nDisciplinas de {aluno1.nome}:")
for d in listar_disciplinas_do_aluno(aluno1, [disciplina1, disciplina2]):
    print("-", d.nome)

print(f"\nAlunos em {disciplina1.nome}:")
for a in listar_alunos_da_disciplina(disciplina1, [aluno1, aluno2]):
    print("-", a.nome)
