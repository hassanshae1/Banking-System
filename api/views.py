
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404

from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import *
from .serializers import *
# Create your views here.

class BranchesAPIView(generics.ListCreateAPIView):
    queryset= Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BankAPIView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class CreateAccountAPIView(APIView):
    def post(self,request):
        """
        {
            "full_name":"Biya Rajpoot",
            "address":"123 Main St",
            "open_date":"2024-02-25",
            "account_type":"current",
            "bank":"1",        
        }
        """
        clint = Clint.objects.create(
            name = request.data['full_name'],
            address = request.data['address']
            
        ) 
        bank = Bank.objects.get(pk=request.data['bank'])
        account = Accounts.objects.create(
            clint = clint,
            open_date = request.data['open_date'],
            account_type = request.data['account_type'],
            bank  = bank
        )



