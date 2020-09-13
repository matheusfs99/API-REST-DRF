import requests

headers = {'Authorization': 'Token 2be852eae8bffabcc5f3a086a8561d125ef32ccc'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}7/', headers=headers)

# Testando o código HTTP
assert resultado.status_code == 204

# Testando se o tamanho do conteudo retornado é 0
assert len(resultado.text) == 0