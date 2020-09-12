import requests

# GET Avaliacoes
# avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
# print(avaliacoes.json()['next'])

# Acessando os resultados dessa página
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))


# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# Acessando o último elemento da lista de resultados
# print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da pessoa que faz a última avaliação
# print(avaliacoes.json()['results'][-1]['nome'])


# GET Avaliação
# avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/5')

# print(avaliacao.json())


# GET Cursos

headers = {'Authorization': 'Token 2be852eae8bffabcc5f3a086a8561d125ef32ccc'}

cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())