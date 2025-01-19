from rest_framework import serializers

from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "name", "description", "video_link", "course"]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ["id", "name", "description", "lessons_count", "lessons"]
