import allure
import requests

from urls import Urls


class GetOrder:
    @allure.step('Получение списка заказов')
    def get_orders_list(self, params=None):
        return requests.get(Urls.URL_orders_create, params=params)


