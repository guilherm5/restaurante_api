from django.urls import path
from . import views

urlpatterns = [
    path('res/getFiscalInvoice/', views.GetFiscalInvoiceAPIView.as_view(), name='get_fiscal_invoice'),
    path('res/getGuestChecks/', views.GetGuestChecksAPIView.as_view(), name='get_guest_checks'),
    path('/trans/getTransactions/', views.GetTransactionsAPIView.as_view(), name='get_transactions'),
]