from django.urls import path
from .views import UsersViewSet

urlpatterns = [
    # user Admin
    path('get/', UsersViewSet.as_view({'get': 'get_all'})),
    path('delete/<int:id>/', UsersViewSet.as_view({'delete': 'delete'})),
    path('get_id/<int:id>/', UsersViewSet.as_view({'get': 'get_by_id'})),
]
