# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import NFT


@admin.register(NFT)
class NFTAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "image", "created_at", "updated_at"]
