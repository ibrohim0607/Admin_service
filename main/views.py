from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
import requests
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema


class UsersViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get all",
        operation_summary="Get all",
        tags=['Admin']
    )
    def get_all(self, request, *args, **kwargs):
        response = requests.get(f"{settings.USER_MANAGEMENT_SERVICE_URL}/getinfo/")
        if response.status_code == 200:
            return Response({'message': 'True'}, status=response.status_code)
        else:
            return Response({'message': 'False'}, status=response.status_code)

    @swagger_auto_schema(
        operation_description="Delete",
        operation_summary="Delete",
        tags=['Admin']
    )
    def delete(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id')

        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        response = requests.post(f"{settings.USER_MANAGEMENT_SERVICE_URL}/delete_user/", data={'user_id': user_id})
        if response.status_code == status.HTTP_200_OK:
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to delete user'}, status=response.status_code)

    @swagger_auto_schema(
        operation_description="Get by id",
        operation_summary="Get by id",
        tags=['Admin']
    )
    def get_by_id(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id')

        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        response = requests.get(f"{settings.USER_MANAGEMENT_SERVICE_URL}/user_details/", data={'user_id': user_id})
        if response.status_code == status.HTTP_200_OK:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to retrieve user details'}, status=response.status_code)


class UserAnalyticsViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get Analytic",
        operation_summary="et Analytic",
        tags=['Admin']
    )
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id')

        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        response = requests.get(f"{settings.ANALYTICS_SERVICE_URL}/user_analytics/", data={'user_id': user_id})
        if response.status_code == 200:
            return Response(response.json(), status=200)
        else:
            return Response({'error': 'Failed to retrieve analytics data'}, status=response.status_code)
