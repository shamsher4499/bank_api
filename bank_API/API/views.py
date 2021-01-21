from django.shortcuts import render
from .models import Bank
from .resources import BankResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from .filters import APIFilter
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BankSerializer
from rest_framework.generics import ListAPIView
from .mypaginations import MyLimitOffsetPagination


# Create your views here.
def simple_api(request):
    if request.method == 'POST':
        bank_resource = BankResource()
        dataset = Dataset()
        new_bank = request.FILES['myfile']

        if not new_bank.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'API/upload.html')

        imported_data = dataset.load(new_bank.read(),format='xlsx')
        for data in imported_data:
            value = Bank(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                )
            value.save()
    return render(request, 'API/upload.html')


def home(request):
    # bank = Bank.objects.all()
    bank = Bank.objects.filter(city='JAIPUR')
    # bank = Bank.objects.order_by('bank_id').reverse()[:5]
    # bank = Bank.objects.values('branch', 'bank_name')
    return render(request, 'API/home.html', {'Bank':bank})

# @api_view(['GET'])
# def banklist(request):
#     # banks = Bank.objects.all()
#     banks = Bank.objects.filter(city='JAIPUR')
#     # banks = Bank.objects.order_by('branch')
#     serializer = BankSerializer(banks, many=True)
#     return Response(serializer.data)

class BankList(ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    pagination_class = MyLimitOffsetPagination


def index(request):
    return render(request, 'API/base.html')