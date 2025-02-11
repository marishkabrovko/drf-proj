from datetime import datetime, timedelta

import pytz
from celery import shared_task

from config.settings import TIME_ZONE
from users.models import User


@shared_task
def check_last_login():
    today = datetime.now(pytz.timezone(TIME_ZONE))
    for user in User.objects.filter(is_active=True):
        if user.last_login:
            if user.last_login + timedelta(days=30) < today:
                user.is_active = False
                user.save()
