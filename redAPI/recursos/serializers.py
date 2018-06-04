from rest_framework import serializers
from . import models


class RecursoSerializer(serializers.ModelSerializer):

    class Meta:

        fields = (
            'id',
            'nombre',
            'descripcion',
        )

        model = models.Recurso