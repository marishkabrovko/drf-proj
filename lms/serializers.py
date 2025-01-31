import urllib.parse

from rest_framework import serializers

from lms.models import Course, Lesson, Subscription
from lms.validators import validate_video_link

from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.CharField(validators=[validate_video_link])

    class Meta:
        model = Lesson
        fields = ["id", "name", "description", "video_link", "course"]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        user = self.context["request"].user
        if not user.is_authenticated:
            return False
        return Subscription.objects.filter(user=user, course=obj).exists()

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "description",
            "lessons_count",
            "lessons",
            "is_subscribed",
        ]
