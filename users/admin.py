from django.contrib import admin

from users.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "course", "lesson", "amount", "payment_method")
    search_fields = ("user", "course", "lesson")
    ordering = ("-date",)
