from django.urls import path
from .views import PaymentInitiateView, PaymentStatusView

urlpatterns = [
    path('v1/payments', PaymentInitiateView.as_view(), name='payment_initiate'),
    path('v1/payments/<uuid:pk>', PaymentStatusView.as_view(), name='payment_status'),
]