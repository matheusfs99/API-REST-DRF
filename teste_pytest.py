import requests

class TesteCursos:
    headers = {'Authorization': 'Token 2be852eae8bffabcc5f3a086a8561d125ef32ccc'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}11/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo_curso = {
            "titulo": "Curso de Programação com Ruby2",
            "url": "http://www.geekuniversity.com.br/cpr2"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo_curso)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo_curso['titulo']

    def test_put_curso(self):
        curso_atualizado = {
            "titulo": "Novo Curso de Ruby 3",
            "url": "http://www.geekuniversity.com.br/ncpr3"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}11/', headers=self.headers, data=curso_atualizado)

        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == curso_atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}11/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0