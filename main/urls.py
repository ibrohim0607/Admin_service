from django.urls import path
from .views import UsersViewSet, PostsViewSet

urlpatterns = [
    # user admin
    path('get/users/', UsersViewSet.as_view({'get': 'get_all'})),
    path('delete/<int:id>/', UsersViewSet.as_view({'delete': 'delete'})),
    path('get/user/<int:id>/', UsersViewSet.as_view({'get': 'get_by_id'})),
    # post admin
    path('posts/', PostsViewSet.as_view({'get': 'get'})),
    path('post/<int:id>/', PostsViewSet.as_view({'get': 'get_by_id'}))

]
