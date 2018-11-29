from django.contrib.auth.models import User, Group
from registro.models import Postulante, Perro
from rest_framework import viewsets
from registro.apirest.serializers import PostulanteSerializer, PerroSerializer


class PostulanteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Postulante.objects.all()
    serializer_class = PostulanteSerializer

class PerroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Perro.objects.all()
    serializer_class = PerroSerializer