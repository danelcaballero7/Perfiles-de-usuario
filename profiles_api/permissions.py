from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Permite usuario editar su propio permiso"""

    def has_object_permission(self, request, view, obj):
        """Chequear si un usuario esta intentando editar su perfil"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """permite actualizar propio status feed"""

    def has_object_permission(self, request, view, obj):
        """Chequear si un usuario esta intentando editar su perfil"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile_id == request.user.id