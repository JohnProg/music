# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(
        verbose_name='Nombre',
        max_length=60
    )
    country = models.CharField(
        verbose_name='País',
        max_length=60
    )



