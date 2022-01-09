from converter.models import Pairing
from converter.utils.rates import get_rates

from itertools import permutations

combs = ["usd", "eur", "pln", "czk"]


def save_to_db():
    if Pairing.objects.all().exists():
        for pairing in permutations(combs, 2):
            updated_pairing = Pairing.objects.get(
                pairing=f"{pairing[0]}-{pairing[1]}"
            )
            updated_pairing.rate = get_rates(pairing[0], pairing[1])[pairing[1]]
            updated_pairing.save()
    else:
        for pairing in permutations(combs, 2):
            new_pairing = Pairing(
                pairing=f"{pairing[0]}-{pairing[1]}",
                rate=get_rates(pairing[0], pairing[1])[pairing[1]]
            )
            new_pairing.save()
