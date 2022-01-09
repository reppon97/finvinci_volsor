from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from converter.forms import CurrencyForm
from converter.models import Pairing


class ConverterTemplateView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "converter/index.html"

    def get(self, request):
        form = CurrencyForm(initial={"c_to": "eur"})

        return Response({"form": form})

    def post(self, request):
        form = CurrencyForm(request.POST)
        if form.is_valid():
            pairing = Pairing.objects.filter(
                pairing=f"{form.cleaned_data['c_from']}-{form.cleaned_data['c_to']}",
            ).first()
            total = float(pairing.rate) * float(form.cleaned_data["amount"])

            return Response({"response": pairing, "total": total})
