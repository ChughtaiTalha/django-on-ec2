# -*- coding: utf-8 -*-
from django.urls import path
from .views import (
    HomePgeView,
    NFTCreateView,
    NFTDetailView,
    NFTUpdateView,
    NFTDeleteView,
    NFTListView,
)

urlpatterns = [
    path("", HomePgeView.as_view(), name="home-page"),
    path("nfts/", NFTListView.as_view(), name="list-nft"),
    path("nft/create/", NFTCreateView.as_view(), name="nft-create"),
    path("nft/<uuid:pk>/", NFTDetailView.as_view(), name="nft-detail"),
    path("nft/<uuid:pk>/update/", NFTUpdateView.as_view(), name="nft-update"),
    path("nft/<uuid:pk>/delete/", NFTDeleteView.as_view(), name="nft-delete"),
]
