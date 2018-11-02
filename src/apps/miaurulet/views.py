from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.miaurulet.constants import SPIN_VALUES
from apps.miaurulet.models import SpinResult


class RuletaView(APIView):
    '''
    Retorna el resultado del spin
    :param request:
    :return:
    '''

    def get(self, request):
        from random import randint
        if request.GET.get('spin'):
            spin = list()
            for spin_index in range(5):
                spin.append([
                    SPIN_VALUES[randint(0, 5)][0],
                    SPIN_VALUES[randint(0, 5)][0],
                    SPIN_VALUES[randint(0, 5)][0],
                ])
            SpinResult(resultado=str(spin))
            return Response(spin)
        return render(
            request, 'web/home.html'
        )
