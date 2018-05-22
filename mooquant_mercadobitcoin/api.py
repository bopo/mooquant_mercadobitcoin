import requests


class MercadobitcoinError(Exception):
    def __init__(self, message, response):
        Exception.__init__(self, message)


def json_http_request(url):
    response = requests.get(url)
    return response.json()


def get_trades():
    # .format(currency_pair)
    url = "https://www.mercadobitcoin.net/api/trades/"

    try:
        ret = json_http_request(url)
    except BaseException:
        raise MercadobitcoinError('Problem fetching trades')

    return ret


def get_orderbook(currency_pair):
    # .format(currency_pair)
    url = "https://www.mercadobitcoin.net/api/orderbook/"

    try:
        ret = json_http_request(url)
    except BaseException:
        raise MercadobitcoinError('Problem fetching trades')

    return ret
