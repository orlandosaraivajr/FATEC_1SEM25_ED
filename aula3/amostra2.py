from collections import UserDict


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.disciplinas = []

    def matricular(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            disciplina.adicionar_aluno(self)

    def __str__(self):
        return f"Aluno: {self.nome} (Matrícula: {self.matricula})"


class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)

    def __str__(self):
        return f"Disciplina: {self.nome} (Código: {self.codigo})"


# === Usando UserDict para gerenciar cadastros ===

class Alunos(UserDict):
    """Dicionário de alunos, chave = matrícula"""
    def adicionar(self, aluno):
        self.data[aluno.matricula] = aluno

    def buscar(self, matricula):
        return self.data.get(matricula)


class Disciplinas(UserDict):
    """Dicionário de disciplinas, chave = código"""
    def adicionar(self, disciplina):
        self.data[disciplina.codigo] = disciplina

    def buscar(self, codigo):
        return self.data.get(codigo)


# ===== Exemplo de uso =====
alunos = Alunos()
disciplinas = Disciplinas()

# Criando e adicionando alunos
a1 = Aluno("Maria", "A001")
a2 = Aluno("João", "A002")
alunos.adicionar(a1)
alunos.adicionar(a2)

# Criando e adicionando disciplinas
d1 = Disciplina("Programação", "D101")
d2 = Disciplina("Estruturas de Dados", "D102")
disciplinas.adicionar(d1)
disciplinas.adicionar(d2)

# Matriculando via objetos recuperados do UserDict
alunos.buscar("A001").matricular(disciplinas.buscar("D101"))
alunos.buscar("A001").matricular(disciplinas.buscar("D102"))
alunos.buscar("A002").matricular(disciplinas.buscar("D101"))

# Exibindo
print("\nDisciplinas de Maria:")
for disc in alunos.buscar("A001").disciplinas:
    print("-", disc.nome)

print("\nAlunos em Programação:")
for al in disciplinas.buscar("D101").alunos:
    print("-", al.nome)
