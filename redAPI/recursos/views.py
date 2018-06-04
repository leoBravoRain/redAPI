# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers

# Create your views here.

# Vista generica para mostrar lista de recursos
class ListaRecursos(generics.ListCreateAPIView):

	queryset = models.Recurso.objects.all()
	serializer_class = serializers.RecursoSerializer
