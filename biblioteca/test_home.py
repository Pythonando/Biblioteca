from django.test import Client

def test_home_status_code(client: Client):
    resposta = client.get('/')
    assert resposta.status_code == 200
