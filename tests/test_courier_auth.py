import allure
import pytest
import requests
import data
import helpers
from urls import Urls


class TestCourierAuth:

    @allure.title('Verify successful courier authentication with required fields filled')
    @allure.description('Checks that a unique identifier id is returned in the response')
    def test_successful_courier_login(self, valid_courier_data_without_firstname):
        requests.post(Urls.URL_courier_create, data=valid_courier_data_without_firstname)
        login_response = requests.post(Urls.URL_courier_login, data=valid_courier_data_without_firstname)
        assert login_response.status_code == 200 and login_response.json()["id"] is not None

    @allure.title('Verify error response for courier authentication with invalid data')
    @allure.description('The test receives sets of data with non-existent login or incorrect password in sequence. '
                        'It checks the response code and body.')
    @pytest.mark.parametrize('field, invalid_value', [('login', helpers.StringGenerator.generate_random_string(10)),
                                                       ('password', helpers.StringGenerator.generate_random_string(10))])
    def test_login_with_nonexistent_data(self, valid_courier_data, field, invalid_value):
        requests.post(Urls.URL_courier_create, data=valid_courier_data)
        valid_courier_data[field] = invalid_value
        login_response = requests.post(Urls.URL_courier_login, data=valid_courier_data)
        assert login_response.status_code == 404 and login_response.json()[
            "message"] == data.Response.RESPONSE_ACCOUNT_NOT_FOUND

    @allure.title('Проверка получения ошибки аутентификации курьера с пустым полем логина или пароля')
    @allure.description('В тест по очереди передаются наборы данных с пустым логином или паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_courier_login_empty_credentials_bad_request(self, valid_courier_data, key, value):
        valid_courier_data[key] = value
        currier_resp = requests.post(Urls.URL_courier_login, data=valid_courier_data)
        assert currier_resp.status_code == 400 and currier_resp.json()[
            "message"] == data.Response.RESPONSE_NO_DATA_INPUT