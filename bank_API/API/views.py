from django.shortcuts import render
from .models import Bank
from .resources import BankResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from .filters import APIFilter

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

    # myFilter = APIFilter(request.GET, queryset=)
    # APIs = myFilter.qs
    # context = {'myFilter':myFilter}

    bank = Bank.objects.all()
    return render(request, 'API/home.html', {'Bank':bank})

class BankList(APIView):
    def get(self, request):
        Bank1 = Bank.objects.all()
        serializer = BankSerializer(Bank1, name=True)
        return Response(serializer.data)

    def post(self):
        pass