from rest_framework import serializers
from .models import * 

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('__all__')

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('__all__')


class ClintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clint
        fields = ('__all__')

class ClintManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClintManager
        fields = ('__all__')

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('__all__')

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('__all__')

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('__all__')

class DepositeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('__all__')

