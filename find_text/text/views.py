from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *

def home(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text == 'Hello':
            return JsonResponse({'success': True, 'message': 'Text Found'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid text input.'})
    return render(request, 'home.html')