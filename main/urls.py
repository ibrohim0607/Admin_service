from django.urls import path
from .views import UsersViewSet, UserAnalyticsViewSet, PostsViewSet

urlpatterns = [
    # user admin
    path('get/', UsersViewSet.as_view({'get': 'get_all'})),
    path('delete/<int:id>/', UsersViewSet.as_view({'delete': 'delete'})),
    path('get_id/<int:id>/', UsersViewSet.as_view({'get': 'get_by_id'})),
    # analytics admin
    path('analytics/', UserAnalyticsViewSet.as_view({'get': 'get'})),
    # post admin
    path('posts/', PostsViewSet.as_view({'get': 'get'})),
    path('post/<int:id>/', PostsViewSet.as_view({'get': 'get_by_id'}))

]
