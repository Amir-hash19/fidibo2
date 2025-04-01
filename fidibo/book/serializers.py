from rest_framework import serializers
from .models import Book



class BookSerializer(serializers.ModelSerializer):
    digital_version_url = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ["title", "author", "price", "status", "digital_version_url"]


    def get_digital_version_url(self, obj):
        if obj.digital_version:
            return obj.digital_version.url
        return None
        


