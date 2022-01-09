from django.urls import path

from converter import views

app_name = "converter"

urlpatterns = [
    path("", views.ConverterTemplateView.as_view(), name="index")
]
