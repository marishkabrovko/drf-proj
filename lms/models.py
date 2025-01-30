from django.db import models

from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Курс", help_text="Введите название курса")
    description = models.TextField(verbose_name="Описание курса", help_text="Введите описание курса", blank=True,
                                   null=True)
    preview = models.ImageField(upload_to="media/img/", verbose_name="Превью курса", help_text="Загрузите превью курса",
                                blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец",
                              help_text="Выберите владельца курса", related_name="courses", null=True, blank=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name="Урок", help_text="Введите название урока")
    description = models.TextField(verbose_name="Описание урока", help_text="Введите описание урока", blank=True,
                                   null=True)
    preview = models.ImageField(upload_to="media/img/", verbose_name="Превью урока",
                                help_text="Загрузите превью урока", blank=True, null=True)
    video_link = models.CharField(verbose_name="Ссылка на урок", help_text="Добавьте ссылку на урок")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name="Курс", help_text="Выберите курс",
                               related_name="lessons", blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец",
                              help_text="Выберите владельца урока", related_name="lessons", null=True, blank=True)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="subscriptions")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", related_name="subscriptions")
    date = models.DateField(verbose_name="Дата подписки", auto_now_add=True)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f'Подписка на курс "{self.course.name}"'
