from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):  # для view MovieAPIUpdate()
    def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:  # если пришедший method это ('GET', 'HEAD', 'OPTIONS') тогда доступ для всех
                return True
            return obj.user == request.user  # иначе, если user из БД (obj.user) = user из запроса (request.user ) то разрешение