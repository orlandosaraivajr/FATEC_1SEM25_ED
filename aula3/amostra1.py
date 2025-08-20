class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.disciplinas = []  # lista de disciplinas em que está matriculado

    def matricular(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            disciplina.adicionar_aluno(self)  # mantém relação bidirecional

    def __str__(self):
        return f"Aluno: {self.nome} (Matrícula: {self.matricula})"


class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []  # lista de alunos matriculados

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)

    def __str__(self):
        return f"Disciplina: {self.nome} (Código: {self.codigo})"


# ===== Exemplo de uso =====

# Criando alunos
aluno1 = Aluno("Maria", "A001")
aluno2 = Aluno("João", "A002")

# Criando disciplinas
disciplina1 = Disciplina("Programação", "D101")
disciplina2 = Disciplina("Estruturas de Dados", "D102")

# Matriculando alunos
aluno1.matricular(disciplina1)
aluno1.matricular(disciplina2)
aluno2.matricular(disciplina1)

# Listando dados
print(aluno1)
print("Disciplinas de Maria:")
for d in aluno1.disciplinas:
    print("-", d.nome)

print("\nAlunos em Programação:")
for a in disciplina1.alunos:
    print("-", a.nome)
