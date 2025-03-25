import allure
import pytest
import requests
from data import Response
from urls import Urls



@allure.story("Создание курьера")
class TestCourierAccountCreation:
    @allure.title('Проверка успешного создания курьера с корректными данными')
    @allure.description('Сценарий "Happy path". Проверка кода и содержимого ответа.')
    def test_create_courier_successfully(self, create_courier):
        pass # Логика реализовано в фикстуре

    @allure.title("Создание курьера с обязательными полями: логин и пароль")
    @allure.description('Проверка кода и содержимого ответа.')
    def test_create_courier_with_required_fields(self, valid_courier_data_without_firstname):
        response = requests.post(Urls.URL_courier_create, data=valid_courier_data_without_firstname)
        assert response.status_code == 201 and response.text == Response.RESPONSE_REGISTRATION_SUCCESSFUL

    @allure.title('Проверка ошибки при повторной регистрации с существующими логином и паролем')
    @allure.description('Проверка кода и содержимого ответа.')
    def test_create_courier_with_taken_login(self, valid_courier_data):
        # Создание первого курьера
        response = requests.post(Urls.URL_courier_create, data=valid_courier_data)
        assert response.status_code == 201 and response.text == Response.RESPONSE_REGISTRATION_SUCCESSFUL

        # Повторная попытка создания
        response = requests.post(Urls.URL_courier_create, data=valid_courier_data)
        assert response.status_code == 409 and response.json()["message"] == Response.RESPONSE_LOGIN_USED

    @allure.title("Ошибка создания курьеров с одинаковыми логинами")
    @allure.description('Проверка кода и содержимого ответа.')
    def test_double_login_courier_creation(self, valid_couriers_data):
        requests.post(Urls.URL_courier_create, data=valid_couriers_data[0])
        response = requests.post(Urls.URL_courier_create, data=valid_couriers_data[1])
        assert response.status_code == 409 and response.json()["message"] == Response.RESPONSE_LOGIN_USED

    @allure.title('Проверка ошибки при отсутствии обязательных полей')
    @allure.description('Проверка кода и содержимого ответа с набором данных, где логин или пароль отсутствует.')
    @pytest.mark.parametrize('field, value', [('login', ''), ('password', '')])
    def test_create_courier_with_empty_fields(self, valid_courier_data, field, value):
        valid_courier_data[field] = value
        response = requests.post(Urls.URL_courier_create, data=valid_courier_data)
        assert response.status_code == 400 and response.json()["message"] == Response.RESPONSE_NO_DATA_ACCOUNT