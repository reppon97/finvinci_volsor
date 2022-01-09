import requests


def get_rates(c_from, c_to):
    page = requests.get(
        f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{c_from}/{c_to}.json"
    )

    return page.json()
