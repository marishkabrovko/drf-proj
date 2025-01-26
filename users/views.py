from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    ordering_fields = ("date",)
    filterset_fields = (
        "course",
        "lesson",
        "payment_method",
    )
