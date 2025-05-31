from db_operations import (
    cadastrar_aluno,
    cadastrar_curso,
    registrar_realizacao
)

# Cadastrar alunos
cadastrar_aluno("João", 22, "ADS", ["Programação", "Scrum"])
cadastrar_aluno("Maria", 23, "ADS", ["Programação", "Nuvem"])
cadastrar_aluno("Pedro", 24, "Psicologia", ["Social", "Educação"])
cadastrar_aluno("Lucas", 23, "CDI", ["Nuvem", "Banco de Dados"])
cadastrar_aluno("Ana", 22, "Medicina", ["Saude"])

# Cadastrar cursos
cadastrar_curso("ADS", "Tecnologia", "Médio")
cadastrar_curso("CDI", "Tecnologia", "Avançado")
cadastrar_curso("Psicologia", "Saude", "Fácil")
cadastrar_curso("Medicina", "Saude", "Avançado")
cadastrar_curso("Educação Fisica", "Saude", "Fácil")

# Registrar realizações
registrar_realizacao("João", "Medicina")
registrar_realizacao("João", "Psicologia")
registrar_realizacao("Maria", "CDI")
registrar_realizacao("Maria", "ADS")
registrar_realizacao("Pedro", "Psicologia")
registrar_realizacao("Pedro", "Medicina")
registrar_realizacao("Ana", "Medicina")
registrar_realizacao("Ana", "Educação Fisica")
registrar_realizacao("Lucas", "CDI")
registrar_realizacao("Lucas", "ADS")
