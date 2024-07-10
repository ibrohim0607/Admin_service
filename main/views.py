from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
import requests
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from .serializer import UserSerializer
from drf_yasg import openapi


class UsersViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get all user",
        operation_summary="Get all user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "token": openapi.Schema(type=openapi.TYPE_STRING, description="Token")
            },
            requiered=["token"]
        ),
        responses={200: UserSerializer(many=True)},
        tags=['Admin']
    )
    def check_token(self, token):
        response = requests.post('http://134.122.76.27:8114/api/v1/check/', data={'token': token})
        if response.status_code != 200:
            raise ValidationError({'error': 'Invalid token'})

    def get_all(self, request, *args, **kwargs):
        self.check_token(request.data.get('token'))
        access_token = request.headers.get('Authorization')
        response_auth = requests.get(f"{settings.USER_MANAGEMENT_SERVICE_URL}/api/v1/auth/me/",
                                     headers={'Authorization': access_token})
        if response_auth.status_code != 200:
            return Response({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        response = requests.get(f"{settings.USER_MANAGEMENT_SERVICE_URL}/getinfo/")
        if response.status_code == 200:
            return Response(response.json(), status=response.status_code)
        else:
            return Response({'message': 'False'}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete user",
        operation_summary="Delete user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "token": openapi.Schema(type=openapi.TYPE_STRING, description="Token"),
                "user_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="User_id")
            },
            requiered=["token", "user_id"]
        ),
        responses={200: UserSerializer()},
        tags=['Admin']
    )
    def delete(self, request, id, *args, **kwargs):
        self.check_token(request.data.get('token'))
        access_token = request.headers.get('Authorization')
        response_auth = requests.get(f"{settings.USER_MANAGEMENT_SERVICE_URL}/api/v1/auth/me/",
                                     headers={'Authorization': access_token})
        if response_auth.status_code != 200:
            return Response({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        if not id:
            return Response({'error': 'user id is required'}, status=status.HTTP_400_BAD_REQUEST)

        response = requests.post(f"{settings.USER_MANAGEMENT_SERVICE_URL}/delete_user/{id}/")
        if response.status_code == 200:
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to delete user'}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Get by id",
        operation_summary="Get by id",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "token": openapi.Schema(type=openapi.TYPE_STRING, description="Token")
            },
            requiered=["token"]
        ),
        responses={200: UserSerializer()},
        tags=['Admin']
    )
    def get_by_id(self, request, id, *args, **kwargs):
        self.check_token(request.data.get('token'))
        access_token = request.headers.get('Authorization')
        response_auth = requests.get(f"{settings.USER_MANAGEMENT_SERVICE_URL}/api/v1/auth/me/",
                                     headers={'Authorization': access_token})
        if response_auth.status_code != 200:
            return Response({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        if not id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        response = requests.get(f"{settings.USER_MANAGEMENT_SERVICE_URL}/user_details/{id}", )
        if response.status_code == 200:
            return Response(response.json(), status=response.status_code)
        else:
            return Response({'error': 'Failed to retrieve user details'}, status=status.HTTP_400_BAD_REQUEST)

