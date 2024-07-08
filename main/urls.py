from django.urls import path
from .views import UsersViewSet, UserAnalyticsViewSet

urlpatterns = [
    path('get/', UsersViewSet.as_view({'get': 'get_all'})),
    path('delete/', UsersViewSet.as_view({'post': 'delete'})),
    path('get_id/', UsersViewSet.as_view({'get': 'get_by_id'})),

    path('analytic/', UserAnalyticsViewSet.as_view({'get': 'get'})),
]
