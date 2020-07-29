from rest_framework import serializers

from core.models import Tag, Ingredient

class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag objects"""
    
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id', )


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for Ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id', )

