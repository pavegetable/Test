from rest_framework import serializers

from .models import Product, Lesson, ViewingHistory


class LessonSerializer(serializers.ModelSerializer):
    viewed_time = serializers.IntegerField(read_only=True, default=0)
    is_watched = serializers.BooleanField(read_only=True, default=False)
    last_viewed = serializers.DateTimeField(read_only=True, default=None)

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video_url', 'duration', 'viewed_time', 'is_watched', 'last_viewed']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']
