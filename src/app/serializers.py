from rest_framework import serializers

from app.models import Blog, GetToken

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class GetTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetToken
        fields = "__all__"