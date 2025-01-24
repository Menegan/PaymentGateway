from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from paystackapi.transaction import Transaction
from django.conf import settings

class PaymentInitiateView(APIView):
    def post(self, request):
        # Deserialize the request data
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            # Create a new Payment object with "pending" status
            payment = serializer.save(status="pending")

            # Generate a unique Paystack reference
            paystack_reference = f"PAYSTACK-{payment.id}"

            # Simulate sending payment info to Paystack
            # Normally, this is where you'd call Paystack's API
            paystack_response = {
                "status": True,
                "message": "Authorization URL created",
                "data": {"authorization_url": f"https://paystack.com/{paystack_reference}"}
            }

            if paystack_response["status"]:
                payment.reference = paystack_reference
                payment.save()
                return Response({
                    "status": "success",
                    "message": "Payment initiated successfully.",
                    "data": paystack_response["data"]
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    "status": "error",
                    "message": "Failed to initiate payment.",
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentStatusView(APIView):
    def get(self, request, pk):
        try:
            payment = Payment.objects.get(pk=pk)
            serializer = PaymentSerializer(payment)
            return Response({
                "status": "success",
                "message": "Payment details retrieved successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Payment not found."
            }, status=status.HTTP_404_NOT_FOUND)