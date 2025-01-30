from django.contrib import admin

from users.models import Payment, User


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "date",
        "course",
        "lesson",
        "amount",
        "payment_method",
    )
    search_fields = ("user", "course", "lesson")
    ordering = ("-date",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
    )
    search_fields = ("email",)
    ordering = ("email",)
