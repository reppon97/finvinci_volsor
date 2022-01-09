from django import forms


# Our form.
class CurrencyForm(forms.Form):
    CHOICES = (
        ("usd", "USD (U.S. Dollars)"),
        ("eur", "EUR (Euro)"),
        ("czk", "CZK (Czech Koruna)"),
        ("pln", "PLN (Polish Zloty)")
    )
    amount = forms.FloatField(widget=forms.NumberInput(attrs={"class": "w-50"}))
    c_from = forms.ChoiceField(choices=CHOICES, label="From")
    c_to = forms.ChoiceField(choices=CHOICES, label="To")
