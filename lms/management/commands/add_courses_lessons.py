from django.core.management import call_command
from django.core.management.base import BaseCommand

from lms.models import Course, Lesson


class Command(BaseCommand):
    help = "Fill the database from fixture"

    def handle(self, *args, **kwargs):
        Course.objects.all().delete()
        Lesson.objects.all().delete()

        call_command("loaddata", "courses_lessons_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
