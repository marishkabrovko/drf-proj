from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = ("date",)
    filterset_fields = ("course", "lesson", "payment_method",)
