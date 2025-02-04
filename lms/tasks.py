from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from lms.models import Subscription, Course


@shared_task
def send_mail_about_update_course(course_id):
    subs = Subscription.objects.filter(course_id=course_id)
    users = [sub.user.email for sub in subs]
    course = Course.objects.get(id=course_id)

    send_mail("Обновление курса", f"Курс \"{course.name}\" был обновлен", EMAIL_HOST_USER, users)
