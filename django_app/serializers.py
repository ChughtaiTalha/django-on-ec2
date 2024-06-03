# -*- coding: utf-8 -*-
# from django import forms
from .models import NFT
from rest_framework import serializers


class NFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFT
        fields = ["name", "price", "image"]
