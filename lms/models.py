from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Курс", help_text="Введите название курса"
    )
    description = models.TextField(
        verbose_name="Описание курса",
        help_text="Введите описание курса",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="media/img/",
        verbose_name="Превью курса",
        help_text="Загрузите превью курса",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Урок", help_text="Введите название урока"
    )
    description = models.TextField(
        verbose_name="Описание урока",
        help_text="Введите описание урока",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="media/img/",
        verbose_name="Превью урока",
        help_text="Загрузите превью урока",
        blank=True,
        null=True,
    )
    video_link = models.CharField(
        verbose_name="Ссылка на урок", help_text="Добавьте ссылку на урок"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text="Выберите курс",
        related_name="lessons",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
