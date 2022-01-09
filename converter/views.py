from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from converter.forms import CurrencyForm
from converter.models import Pairing


# Our template view. Data is taken from DB.
class ConverterTemplateView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "converter/index.html"

    # GET method.
    def get(self, request):

        # set initial to "eur" to prevent possible error
        form = CurrencyForm(initial={"c_to": "eur"})

        return Response({"form": form})

    # POST method.
    def post(self, request):
        form = CurrencyForm(request.POST)
        if form.is_valid():
            c_from = form.cleaned_data["c_from"]
            c_to = form.cleaned_data["c_to"]

            # Check if chosen currency are the same in choicefield
            if c_from == c_to:
                return Response(
                    {"message": "No such pairing."}, status=status.HTTP_404_NOT_FOUND
                )
            pairing = Pairing.objects.filter(
                pairing=f"{form.cleaned_data['c_from']}-{form.cleaned_data['c_to']}",
            ).first()

            # Multiplying amount to the conversion rate and passing it to the template
            total = float(pairing.rate) * float(form.cleaned_data["amount"])

            return Response({"response": pairing, "total": total})
