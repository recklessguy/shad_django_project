from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
# Create your models here.
class ghazals_home(models.Model):
    ghazal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    writer = models.CharField(max_length=100)
    shayari = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering= ('-created',)

    def __str__(Self):
        return Self.name


class new_ghazals(models.Model):
    ghazal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    writer = models.CharField(max_length=100)
    shayari = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    verification_status = models.BooleanField(default=False)

    class Meta:
        ordering= ('-created',)

    def __str__(Self):
        return Self.name

    def get_absolute_url(self):
        return reverse("new-ghazals")

        


class famous_ghazals(models.Model):
    ghazal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    writer = models.CharField(max_length=100)
    shayari = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering= ('-created',)

    def __str__(Self):
        return Self.name
