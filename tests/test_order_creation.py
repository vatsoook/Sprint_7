import pytest
import allure
import requests
import json
from urls import Urls
from data import OrderData

class TestOrderCreation:
    @allure.title("Тестирование процесса создания заказа с возможностью выбора одного цвета, обоих цветов или без указания цвета")
    @allure.description('Согласно требованиям, система должна позволять указать в заказе один цвет самоката, выбрать '
                        'сразу оба или не указывать совсем. В тест по очереди передаются наборы данных с разными '
                        'параметрами: серый, черный, оба цвета, цвет не указан. Проверяются код и тело ответа.')
    @pytest.mark.parametrize('color', OrderData.color_scooter)
    def test_order_creation_with_color_selection(self, color):
        order_payload = OrderData.order_data
        order_payload['color'] = color
        order_payload_json = json.dumps(order_payload)
        response = requests.post(Urls.URL_orders_create, data=order_payload_json)
        response_json = response.json()
        assert response.status_code == 201 and 'track' in response_json.keys()