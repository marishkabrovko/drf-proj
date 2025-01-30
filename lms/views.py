from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course, Lesson, Subscription
from lms.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerators, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

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

    def perform_create(self, serializer):
        lesson = serializer.save(owner=self.request.user)


class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerators | IsOwner]


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

    def post(self, request):
        user_id = request.user.pk
        course_id = request.data["course"].pk
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = course_item.subscriptions.filter(user=user_id)

        if subs_item.exists():
            Subscription.objects.filter(user=user_id, course=course_id).delete()
            message = 'Подписка удалена'
        else:
            Subscription.objects.create(user=user_id, course=course_id)
            message = 'Подписка добавлена'

        return Response({"message": message})
