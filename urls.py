class Urls:
    URL_basic = 'https://qa-scooter.praktikum-services.ru/'
    URL_courier_create = f'{URL_basic}api/v1/courier/'
    URL_courier_login = f'{URL_basic}api/v1/courier/login'
    URL_orders_create = f'{URL_basic}api/v1/orders'
    URL_order_get_number = f'{URL_basic}/api/v1/orders/track'
    URL_order_accept = f'{URL_basic}/api/v1/orders/accept'
    URL_get_list_orders = f'{URL_basic}/api/v1/orders?courierId='