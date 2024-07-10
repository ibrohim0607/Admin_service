from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    gender = serializers.IntegerField()
    workplace = serializers.CharField(max_length=50)


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.IntegerField()
    title = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=500)
    image = serializers.ImageField(blank=True, null=True, required=True)
    like_count = serializers.IntegerField()
    comment_count = serializers.IntegerField()
    view_count = serializers.IntegerField()
    category = serializers.IntegerField()
