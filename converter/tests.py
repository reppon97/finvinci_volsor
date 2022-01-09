from django.test import TestCase

from converter.models import Pairing


# Essential tests for our Pairing model.
class PairingTestCase(TestCase):
    def setUp(self):
        Pairing.objects.create(pairing="usd-eur", rate=0.5)
        Pairing.objects.create(pairing="try-btc", rate=12.55)
        Pairing.objects.create(pairing="czk-pln", rate=10.01)
        Pairing.objects.create(pairing="mkd-aed", rate=32.32)

    def test_pairing_rates(self):
        usd_eur = Pairing.objects.get(pairing="usd-eur")
        try_btc = Pairing.objects.get(pairing="try-btc")
        self.assertEqual(usd_eur.rate, 0.5)
        self.assertEqual(try_btc.rate, 12.55)

    def test_pairing_names(self):
        czk_pln = Pairing.objects.get(pairing="czk-pln")
        mkd_aed = Pairing.objects.get(pairing="mkd-aed")
        self.assertEqual(czk_pln.pairing, "czk-pln")
        self.assertEqual(mkd_aed.pairing, "mkd-aed")
