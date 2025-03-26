import allure
import api_test


class TestListOrder:
    @allure.title("Получение списка заказов")
    def test_fetch_order_list(self):
        request_body = api_test.GetOrder.get_orders_list(self)
        response_data = api_test.GetOrder.get_orders_list(request_body)
        assert 200 == response_data.status_code and type(response_data.json()["orders"]) == list