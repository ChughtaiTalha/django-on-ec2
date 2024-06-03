# -*- coding: utf-8 -*-
from django import forms
from .models import NFT


class NFTForm(forms.ModelForm):
    class Meta:
        model = NFT
        fields = ["name", "price", "image"]
