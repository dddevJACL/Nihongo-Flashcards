from rest_framework.serializers import ModelSerializer
from .models import VocabularyCard


class VocabCardSerializer(ModelSerializer):
    class Meta:
        model = VocabularyCard
        fields = '__all__'