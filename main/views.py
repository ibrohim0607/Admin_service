from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
import requests
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from .serializer import UserSerializer, PostSerializer
from rest_framework import status


class UsersViewSet(ViewSet):
    def get_token(self):
        response = requests.post('http://134.122.76.27:8114/api/v1/login/', json={
            "service_id": 3,
            "service_name": "Admin",
            "secret_key": "c1879710-11ff-4c24-b0ec-f7475cdef1e7"
        })
        return response

    @swagger_auto_schema(
        operation_description="Get all user",
        operation_summary="Get all user",
        responses={200: UserSerializer(many=True)},
        tags=['User']
    )
    def get_all(self, request, *args, **kwargs):
        print(request.data)
        response = requests.post(f"{settings.USER_MANAGEMENT_SERVICE_URL}/get/users/",
                                 json={"token": str(self.get_token().json().get('token'))})
        if response.status_code != 200:
            return Response({"error": "Can not get data"}, status=response.status_code)
        print(response)

        return Response(response.json())

    @swagger_auto_schema(
        operation_description="Delete user",
        operation_summary="Delete user",
        responses={200: UserSerializer()},
        tags=['User']
    )
    def delete(self, request, id, *args, **kwargs):

        response = requests.delete(f"{settings.USER_MANAGEMENT_SERVICE_URL}/delete/user/{id}/",
                                   json={"token": str(self.get_token().json().get('token'))})
        if response.status_code == 200:
            return Response({'message': 'user deleted'}, status=status.HTTP_200_OK)
        return Response({'message': 'user not deleted'}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Get by  user id",
        operation_summary="Get by user id",
        responses={
            200: UserSerializer(),
            404: "Not found"
        },
        tags=['User']
    )
    def get_by_id(self, request, id, *args, **kwargs):
        response = requests.post(f"{settings.USER_MANAGEMENT_SERVICE_URL}/get/user/{id}/",
                                 json={"token": str(self.get_token().json().get('token'))})
        print(response)
        if response.status_code == 200:
            return Response(response.json())
        return Response({"error": "Can not get data"}, status=response.status_code)


class PostsViewSet(ViewSet):
    def get_token(self):
        response = requests.post('http://134.122.76.27:8114/api/v1/login/', json={
            "service_id": 3,
            "service_name": "Admin",
            "secret_key": "c1879710-11ff-4c24-b0ec-f7475cdef1e7"
        })
        return response

    @swagger_auto_schema(
        operation_description="Get all Posts",
        operation_summary="Get all Posts",
        responses={
            200: PostSerializer(many=True),
            404: "Not found"
        },
        tags=['Post']
    )
    def get_all(self, request, *args, **kwargs):
        response = requests.post(f"{settings.POSTS_SERVICE_URL}/posts/list/",
                                 json={"token": str(self.get_token().json().get('token'))})
        print(response)
        if response.status_code != 200:
            return Response({"error": "Can not get data"}, status=response.status_code)
        return Response(response.json())

    @swagger_auto_schema(
        operation_description="Get by  post id",
        operation_summary="Get by post id",
        responses={
            200: PostSerializer(),
            404: "Not found"
        },
        tags=['Post']
    )
    def get_by_id(self, request, id, *args, **kwargs):
        response = requests.post(f"{settings.POSTS_SERVICE_URL}/post/detail-delete/{id}/",
                                 data={"token": str(self.get_token().json().get('token'))})
        return Response(response.json())

    @swagger_auto_schema(
        operation_description="Delete post",
        operation_summary="Delete post",
        responses={200: PostSerializer()},
        tags=['Post']
    )
    def delete_post(self, request, id, *args, **kwargs):

        response = requests.delete(f"{settings.POSTS_SERVICE_URL}/post/detail-delete/{id}/",
                                   json={"token": str(self.get_token().json().get('token'))})
        print(response)
        if response.status_code == 200:
            return Response({'message': 'post deleted'}, status=status.HTTP_200_OK)
        return Response({'message': 'post not deleted'}, status=status.HTTP_400_BAD_REQUEST)
