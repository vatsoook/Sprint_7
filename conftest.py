import pytest
import requests
import helpers
from data import Response
from urls import Urls


@pytest.fixture
#Генерирует данные курьера со случайным логином, паролем и именем.
def valid_courier_data():
    data_courier = helpers.CourierDataGenerator()
    return data_courier.generate_random_data_courier()



@pytest.fixture
#Создает двух курьеров с одинаковым логином.
def valid_couriers_data():
    data_courier_1 = helpers.CourierDataGenerator()
    data_courier_2 = helpers.CourierDataGenerator()
    return (
        data_courier_1.generate_data_courier_static_login(),
        data_courier_2.generate_data_courier_static_login()
    )


@pytest.fixture
#Создает курьера только с логином и паролем, без имени.
def valid_courier_data_without_firstname(valid_courier_data):
    valid_courier_data['firstName'] = ''
    return valid_courier_data


@pytest.fixture
def create_courier(valid_courier_data):
    response = requests.post(Urls.URL_courier_create, data=valid_courier_data)
    assert response.status_code == 201 and response.text == Response.RESPONSE_REGISTRATION_SUCCESSFUL

    # Аутентификация курьера для получения его ID
    login_response = requests.post(Urls.URL_courier_login, data={
        "login": valid_courier_data["login"],
        "password": valid_courier_data["password"]
    })

    courier_id = login_response.json()["id"]
    yield courier_id

    # Удаление курьера после теста
    delete_response = requests.delete(f"{Urls.URL_courier_create}{courier_id}")
    assert delete_response.status_code == 200


@pytest.fixture
def create_valid_courier(valid_courier_data_without_firstname):
    response = requests.post(Urls.URL_courier_create, data=valid_courier_data_without_firstname)
    assert response.status_code == 201
    return valid_courier_data_without_firstname



