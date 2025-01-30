from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course, Lesson, Subscription
from lms.paginators import LessonCoursePagination
from lms.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerators, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = LessonCoursePagination

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (IsAuthenticated, ~IsModerators)
        elif self.action in ["update", "retrieve", "list"]:
            self.permission_classes = (IsAuthenticated, IsModerators | IsOwner)
        elif self.action == "destroy":
            self.permission_classes = (IsAuthenticated, IsOwner, ~IsModerators)

        return super().get_permissions()

    def perform_create(self, serializer):
        course = serializer.save(owner=self.request.user)


class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerators]
    pagination_class = LessonCoursePagination

    def perform_create(self, serializer):
        lesson = serializer.save(owner=self.request.user)


class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerators | IsOwner]
    pagination_class = LessonCoursePagination


class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerators | IsOwner]


class LessonUpdateView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerators | IsOwner]


class LessonDeleteView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerators | IsOwner]


class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user  # ✅ Теперь это объект User
        course_id = request.data.get("course")

        if not course_id:
            return Response({"error": "Поле 'course' обязательно"}, status=400)

        course = get_object_or_404(Course, pk=course_id)  # ✅ Теперь это объект Course

        subscription = Subscription.objects.filter(user=user, course=course)

        if subscription.exists():
            subscription.delete()
            message = "Подписка удалена"
        else:
            Subscription.objects.create(user=user, course=course)  # ✅ Передаём объекты
            message = "Подписка добавлена"

        return Response({"message": message}, status=200)

