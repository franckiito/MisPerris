from django.contrib.auth.models import User, Group
from registro.models import Postulante, Perro
from rest_framework import serializers


class PostulanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Postulante
        fields = ('url', 'run', 'nombre', 'correo', 'fecha')

class PerroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perro
        fields = ('url', 'nombre', 'raza')


