from rest_framework.permissions import BasePermission


class IsModerators(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Moderators").exists()
