from django.urls import path, re_path
from api import views

from .views import (
    BranchesAPIView,
    BranchDetailAPIView,
    BankAPIView,
    BankDetailAPIView,
    # CreateAccountAPIView,
    # AccountListAPIView
)

urlpatterns = [
    path('branches/', BranchesAPIView.as_view(), name='branches'),
    re_path(r'^branch/(?P<pk>[0-9]+)/', BranchDetailAPIView.as_view(), name='branch-detail'),
    path('bank/', BankAPIView.as_view(), name='banks'),
    re_path(r'^bank/(?P<pk>[0-9]+)/', BankDetailAPIView.as_view(), name='bank-detail'),
    # path('create_account/', CreateAccountAPIView.as_view(), name='create-account'),
    # path('accounts/', AccountListAPIView.as_view(), name='accounts'),
]
