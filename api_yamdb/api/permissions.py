from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthOrAdmins(BasePermission):
    """
    Права на изменение данных пользователя:
    Только админ или владелец токена могут менять данные профиля.
    """

    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.is_admin)

    def has_object_permission(self, request, view, obj):
        return (obj == request.user
                or request.user.is_admin)


class OwnResourcePermission(BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user
                or request.method in permissions.SAFE_METHODS
                or request.user.is_moderator
                or request.user.is_admin)


class IsAdminOrReadOnly(BasePermission):
    """
    Проверяет права пользователя на доступ к изменениям данных.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return (request.user.is_authenticated
                and request.user.is_admin)
