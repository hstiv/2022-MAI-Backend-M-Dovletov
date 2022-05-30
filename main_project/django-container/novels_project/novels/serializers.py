from novels.models import Author, Novel
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ['id', 'name', 'bio', 'country']


class NovelSerializer(serializers.ModelSerializer):
	author = serializers.StringRelatedField()
	class Meta:
		model = Novel
		fields = ['id', 'title', 'original_title', 'description', 'author']