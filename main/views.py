from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
import requests
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from .serializer import UserSerializer, PostSerializer
from drf_yasg import openapi


class UsersViewSet(ViewSet):

    def check_token(self, token):
        response = requests.post('http://134.122.76.27:8114/api/v1/check/', data={'token': token})
        if response.status_code != 200:
            raise ValidationError({'error': 'Invalid token'})

    @swagger_auto_schema(
        operation_description="Get all user",
        operation_summary="Get all user",
        responses={200: UserSerializer(many=True)},
        tags=['User']
    )
    def get_all(self, request, *args, **kwargs):
        response = requests.get(f"{settings.USER_MANAGEMENT_SERVICE_URL}/getinfo/")
        return Response(response.json())

    @swagger_auto_schema(
        operation_description="Delete user",
        operation_summary="Delete user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "token": openapi.Schema(type=openapi.TYPE_STRING, title="Token"),
                "user_id": openapi.Schema(type=openapi.TYPE_INTEGER, title="User_id")
            },
            requiered=["token", "user_id"]
        ),
        responses={200: UserSerializer()},
        tags=['User']
    )
    def delete(self, request, id, *args, **kwargs):
        self.check_token(request.data.get('token'))
        access_token = request.headers.get('Authorization')
        response_auth = requests.get(f"{settings.USER_MANAGEMENT_SERVICE_URL}/api/v1/auth/me/",
                                     headers={'Authorization': access_token})
        if response_auth.status_code != 200:
            return Response({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

        if not id:
            return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)

        response = requests.post(f"{settings.USER_MANAGEMENT_SERVICE_URL}/delete_user/{id}/")
        return Response(response.json())

    @swagger_auto_schema(
        operation_description="Get by  user id",
        operation_summary="Get by user id",
        manual_parameters=[
            openapi.Parameter('id', type=openapi.TYPE_INTEGER, description='get user by id',
                              in_=openapi.IN_QUERY,
                              required=True),
        ],
        responses={
            200: UserSerializer(),
            404: "Not found"
        },
        tags=['User']
    )
    def get_by_id(self, request, id, *args, **kwargs):
        if not id:
            return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)

        response = requests.get(f"{settings.USER_MANAGEMENT_SERVICE_URL}/user/{id}/", )
        return Response(response.json())


class UserAnalyticsViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get Analytic",
        operation_summary="Get Analytic",
        # responses={200: UserSerializer(many=True)},
        tags=['Analytic']
    )
    def get(self, request, *args, **kwargs):
        response = requests.get(f"{settings.ANALYTICS_SERVICE_URL}/user_analytics/", )
        return Response(response.json())


class PostsViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get all Posts",
        operation_summary="Get all Posts",
        responses={
            200: PostSerializer(),
            404: "Not found"
        },
        tags=['Post']
    )
    def get(self, request, *args, **kwargs):
        response = requests.get(f"{settings.POSTS_SERVICE_URL}/posts/")
        return Response(response.json())

    @swagger_auto_schema(
        operation_description="Get by  post id",
        operation_summary="Get by post id",
        manual_parameters=[
            openapi.Parameter('id', type=openapi.TYPE_INTEGER, description='get post by id',
                              in_=openapi.IN_QUERY,
                              required=True),
        ],
        responses={
            200: PostSerializer(),
            404: "Not found"
        },
        tags=['Post']
    )
    def get_by_id(self, request, id, *args, **kwargs):
        if not id:
            return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)

        url = f"{settings.POSTS_SERVICE_URL}/post/{id}/"
        response = requests.get(url).json()
        return Response(response)
