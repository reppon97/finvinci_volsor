from converter.models import Pairing
from converter.utils.rates import get_rates

from itertools import permutations

combs = ["usd", "eur", "pln", "czk"]


# Function which saves conversion rates to DB.
def save_to_db():
    # Checking if records exist before creating new ones.
    if Pairing.objects.all().exists():
        # Used permutations to get every possible combinations except x-x.
        for pairing in permutations(combs, 2):
            updated_pairing = Pairing.objects.get(
                pairing=f"{pairing[0]}-{pairing[1]}"
            )
            updated_pairing.rate = get_rates(pairing[0], pairing[1])[pairing[1]]
            updated_pairing.save()

    # Creating new pairings if table is empty.
    else:
        for pairing in permutations(combs, 2):
            new_pairing = Pairing(
                pairing=f"{pairing[0]}-{pairing[1]}",
                rate=get_rates(pairing[0], pairing[1])[pairing[1]]
            )
            new_pairing.save()
