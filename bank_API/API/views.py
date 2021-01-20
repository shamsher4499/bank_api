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
    # bank = Bank.objects.filter(city='JAIPUR')
    # bank = Bank.objects.order_by('bank_id').reverse()[:5]
    bank = Bank.objects.values('branch', 'bank_name')
    return render(request, 'API/home.html', {'Bank':bank})

# class BankList(APIView):
#     def get(self, request):
#         Bank1 = Bank.objects.all()
#         serializer = BankSerializer(Bank1, name=True)
#         return Response(serializer.data)

#     def post(self):
#         pass


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Details View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/</str:pk>/',
        }
    return Response(api_urls)

@api_view(['GET'])
def banklist(request):
    # banks = Bank.objects.all()
    # banks = Bank.objects.filter(city='JAIPUR')
    banks = Bank.objects.order_by('branch')
    serializer = BankSerializer(banks, many=True)
    return Response(serializer.data)