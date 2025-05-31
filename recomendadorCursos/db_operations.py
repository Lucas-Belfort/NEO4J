from config import Neo4jConnection

conn = Neo4jConnection()  # Agora sem passar argumentos!


def cadastrar_aluno(nome, idade, curso, interesses):
    try:
        query = """
        CREATE (a:Aluno {nome: $nome, idade: $idade, curso: $curso, interesses: $interesses})
        """
        conn.query(query, {"nome": nome, "idade": idade, "curso": curso, "interesses": interesses})
    except Exception as e:
        print(f"Erro ao cadastrar aluno: {e}")

def cadastrar_curso(nome, area, dificuldade):
    try:
        query = """
        CREATE (c:Curso {nome: $nome, area: $area, dificuldade: $dificuldade})
        """
        conn.query(query, {"nome": nome, "area": area, "dificuldade": dificuldade})
    except Exception as e:
        print(f"Erro ao cadastrar curso: {e}")

def registrar_realizacao(aluno_nome, curso_nome):
    try:
        query = """
        MATCH (a:Aluno {nome: $aluno_nome}), (c:Curso {nome: $curso_nome})
        MERGE (a)-[:REALIZOU]->(c)
        """
        conn.query(query, {"aluno_nome": aluno_nome, "curso_nome": curso_nome})
    except Exception as e:
        print(f"Erro ao registrar realização: {e}")

def recomendar_cursos(aluno_nome):
    conn = Neo4jConnection()
    try:
        query = """
        MATCH (a1:Aluno {nome: $aluno_nome})-[:REALIZOU]->(c:Curso)<-[:REALIZOU]-(a2:Aluno)
        WHERE a1 <> a2 AND abs(a1.idade - a2.idade) <= 3
        MATCH (a2)-[:REALIZOU]->(recomendado:Curso)
        WHERE NOT (a1)-[:REALIZOU]->(recomendado)
        RETURN DISTINCT recomendado.nome AS cursoRecomendado, recomendado.area AS area, recomendado.dificuldade AS dificuldade
        LIMIT 5
        """
        results = conn.query(query, {"aluno_nome": aluno_nome})
        for record in results:
            print(f"Curso recomendado: {record['cursoRecomendado']} - Área: {record['area']} - Dificuldade: {record['dificuldade']}")
    except Exception as e:
        print(f"Erro ao recomendar cursos: {e}")
    finally:
        conn.close()


def listar_cursos():
    conn = Neo4jConnection()
    query = "MATCH (c:Curso) RETURN c.nome AS nome, c.area AS area, c.dificuldade AS dificuldade"
    results = conn.query(query)
    print("\n--- Cursos Cadastrados ---")
    for curso in results:
        print(f"Título: {curso['nome']} | Área: {curso['area']} | Nível: {curso['dificuldade']}")
    conn.close()


def listar_alunos():
    conn = Neo4jConnection()
    query = "MATCH (a:Aluno) RETURN a.nome AS nome, a.idade AS idade, a.curso AS curso"
    results = conn.query(query)
    print("\n--- Alunos Cadastrados ---")
    for aluno in results:
        print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")
    conn.close()