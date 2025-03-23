import pytest
import helpers


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