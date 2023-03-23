from rest_framework import serializers
from .models import Pizzeria, Image
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


UserModel = get_user_model()


class PizzeriaListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name',
            'city',
            'absolute_url',
        ]
    
    def get_absolute_url(self, obj):
        return reverse('pizzeria_detail', args=(obj.pk,))

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ['id', 'image', 'image_title', 'uploaded_at']
        model = Image


class PizzerDetailSerializer(serializers.ModelSerializer):
    update = serializers.SerializerMethodField()
    delete = serializers.SerializerMethodField()
    pizzeria_images = ImageSerializer(many=True, required=False)
                      

    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name',
            'city',
            'street',
            'description',
            'logo_image',
            'active',
            'update',
            'delete',
            'pizzeria_images',
        ]
    
    def get_update(self, obj):
        return reverse('pizzeria_update', args=(obj.pk,))
    
    def get_delete(self, obj):
        return reverse('pizzeria_delete', args=(obj.pk,))


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
        username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        new_token = Token.objects.create(user=user)
        return user
    class Meta:
        model = get_user_model()
        fields = [ "username", "password"]

