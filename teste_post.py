import requests

headers = {'Authorization': 'Token 2be852eae8bffabcc5f3a086a8561d125ef32ccc'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Gerência Ágil de Projetos com Scrum 2",
    "url": "http://www.geekuniversity.com/scrum2"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)


# Testando o código de status HTTP 201
assert resultado.status_code == 201

# Testando se o título do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']