from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import PaymentListView, UserCreateAPIView, UserListView, UserDetailView, UserUpdateView, UserDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path("payments/", PaymentListView.as_view(), name="payments"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("", UserListView.as_view(), name="users"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user"),
    path("user/<int:pk>/update/", UserUpdateView.as_view(), name="update_user"),
    path("user/<int:pk>/delete/", UserDeleteView.as_view(), name="delete_user"),
]
