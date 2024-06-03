# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import NFT
from .forms import NFTForm


class HomePgeView(View):
    def get(self, request):
        return render(request, "django_app/index.html")


class NFTListView(View):
    def get(self, request):
        nfts = NFT.objects.all()
        return render(request, "django_app/nft_list.html", {"nfts": nfts})


class NFTCreateView(View):
    def get(self, request):
        form = NFTForm()
        return render(request, "django_app/nft_create.html", {"form": form})

    def post(self, request):
        form = NFTForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("nft-list")
        return render(request, "django_app/nft_create.html", {"form": form})


class NFTDetailView(View):
    def get(self, request, pk):
        nft = get_object_or_404(NFT, pk=pk)
        return render(request, "django_app/nft_detail.html", {"nft": nft})


class NFTUpdateView(View):
    def get(self, request, pk):
        nft = get_object_or_404(NFT, pk=pk)
        form = NFTForm(instance=nft)
        return render(request, "django_app/nft_update.html", {"form": form, "nft": nft})

    def post(self, request, pk):
        nft = get_object_or_404(NFT, pk=pk)
        form = NFTForm(request.POST, request.FILES, instance=nft)
        if form.is_valid():
            form.save()
            return redirect("nft-list")
        return render(request, "django_app/nft_update.html", {"form": form, "nft": nft})


class NFTDeleteView(View):
    def get(self, request, pk):
        nft = get_object_or_404(NFT, pk=pk)
        return render(request, "django_app/nft_confirm_delete.html", {"nft": nft})

    def post(self, request, pk):
        nft = get_object_or_404(NFT, pk=pk)
        nft.delete()
        return redirect("nft-list")
