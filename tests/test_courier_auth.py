import allure
import pytest
import requests
import data
import helpers
from urls import Urls


class TestCourierAuth:

    @allure.title('Проверка успешной аутентификации курьера при заполнении необходимых полей')
    @allure.description('Проверяется что в ответ он получит уникальный идентификатор id')
    def test_successful_courier_login(self, create_valid_courier):
        login_response = requests.post(Urls.URL_courier_login, data=create_valid_courier)
        assert login_response.status_code == 200 and login_response.json()["id"] is not None

    @allure.title('Проверка получения ошибки аутентификации курьера при вводе невалидных данных')
    @allure.description('В тест по очереди передаются наборы данных с несуществующим логином или неверным паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('field, invalid_value', [('login', helpers.StringGenerator.generate_random_string(10)),
                                                       ('password', helpers.StringGenerator.generate_random_string(10))])
    def test_login_with_nonexistent_data(self, create_valid_courier, field, invalid_value, valid_courier_data):
        valid_courier_data = create_valid_courier.copy()
        valid_courier_data[field] = invalid_value
        login_response = requests.post(Urls.URL_courier_login, data=valid_courier_data)
        assert login_response.status_code == 404 and login_response.json()[
            "message"] == data.Response.RESPONSE_ACCOUNT_NOT_FOUND

    @allure.title('Проверка получения ошибки аутентификации курьера с пустым полем логина или пароля')
    @allure.description('В тест по очереди передаются наборы данных с пустым логином или паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_courier_login_empty_credentials_bad_request(self, create_valid_courier, key, value, valid_courier_data):
        valid_courier_data = create_valid_courier.copy()
        valid_courier_data[key] = value
        currier_resp = requests.post(Urls.URL_courier_login, data=valid_courier_data)
        assert currier_resp.status_code == 400 and currier_resp.json()[
            "message"] == data.Response.RESPONSE_NO_DATA_INPUT