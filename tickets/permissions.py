from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    """ this permission to apply only user
    not any user can edit your post
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user