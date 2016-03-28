from rest_framework import serializers
from .models import *


class DocumentSerializer(serializers.Serializer):
	class Meta:
		model = Document
