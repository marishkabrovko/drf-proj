from rest_framework import serializers


def validate_video_link(value):
    if not value.startswith("https://www.youtube.com/"):

        raise serializers.ValidationError("Неверная ссылка на видео. Добавьте ссылку на видео с Youtube")
