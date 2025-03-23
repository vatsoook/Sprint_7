import allure
import helpers


class TestListOrder:
    @allure.title("Testing the retrieval of order list")
    def test_fetch_order_list(self):
        request_body = helpers.GetOrder.set_param_order_list(self)
        response_data = helpers.GetOrder.get_orders_list(request_body)
        assert 200 == response_data.status_code and type(response_data.json()["orders"]) == list