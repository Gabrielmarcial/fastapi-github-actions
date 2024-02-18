from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message':'hello'}

def test_get_items_deve_retornar_success():
    response = client.get("/get-items")
    assert response.status_code == 200
    assert response.json()['status'] == "success"
    assert type(response.json()['data']) == list

def test_get_product_deve_retornar_success():
    response = client.get("/get-product/Smartphone")
    assert response.status_code == 200
    assert response.json()['status'] == "success"
    assert type(response.json()['data']) == list

def test_get_price_deve_retornar_success():
    response = client.get("/get-product/Smartphone")
    assert response.status_code == 200
    assert response.json()['status'] == "success"
    assert type(response.json()['data']) == list

def test_get_product_deve_retornar_item_nao_encontrado():
    response = client.get("/get-product/product")
    assert response.status_code == 200
    assert response.json()['status'] == "success"
    assert response.json()['message'] == 'Item não encontrado'

def test_get_price_deve_retornar_item_nao_encontrado():
    response = client.get("/get-price/product")
    assert response.status_code == 200
    assert response.json()['status'] == "success"
    assert response.json()['message'] == 'Preco não encontrado'
