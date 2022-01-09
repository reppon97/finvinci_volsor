import requests


# Function which gets conversion rates from the public API.
def get_rates(c_from, c_to):
    """
    :param c_from:
    :param c_to:
    :return: JSON response with date and rate values.
    """
    page = requests.get(
        f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{c_from}/{c_to}.json"
    )

    return page.json()
