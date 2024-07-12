from django.urls import path
from .views import UsersViewSet, PostsViewSet

urlpatterns = [
    # user admin
    path('get/users/', UsersViewSet.as_view({'get': 'get_all'})),
    path('delete/user/<int:id>/', UsersViewSet.as_view({'delete': 'delete'})),
    path('get/user/<int:id>/', UsersViewSet.as_view({'get': 'get_by_id'})),
    # post admin
    path('posts/', PostsViewSet.as_view({'get': 'get_all'})),
    path('post/<int:id>/', PostsViewSet.as_view({'get': 'get_by_id'})),
    path('delete/post/<int:id>/', PostsViewSet.as_view({'delete': 'delete_post'}))

]
