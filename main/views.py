from django.shortcuts import render

from django.http import HttpResponse
from django.conf import settings
import os

def game_page(request):
    return render(request, 'game_page.html')




def serve_ads_txt(request):
    file_path = os.path.join(settings.BASE_DIR, 'ads.txt')

    # Open the file and return its content
    with open(file_path, 'r') as f:
        content = f.read()

    return HttpResponse(content, content_type='text/plain')

