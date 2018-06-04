# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Recurso(models.Model):

	nombre = models.CharField(max_length = 500)
	descripcion = models.CharField(max_length= 3000)


	# String representation of the model
	def __str__(self):

		return self.nombre
