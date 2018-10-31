from django.urls import path, include
from apps.miaurulet.views import RuletaView

urlpatterns = [
    path('', RuletaView.as_view(), name='ruleta')
]