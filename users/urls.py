from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentListView

app_name = UsersConfig.name

urlpatterns = [
    path("payments/", PaymentListView.as_view(), name="payments"),
]
