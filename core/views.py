from django.shortcuts import render, redirect
from django.http import JsonResponse


def index(request):
    return render(request, 'core/index.html')


def donate(request):
    pass


def successPage(request, args):
    pass


def cardDetail(request):
    pass