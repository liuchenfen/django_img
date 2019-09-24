from django.shortcuts import render

from .createimg import generate
# Create your views here.
from django.http import HttpResponse
from django.urls.base import reverse

def index(request):
    example = reverse('placeholder',kwargs={'width':50,'height':50})
    context = { 'example':request.build_absolute_uri(example)}
    return render(request,'home.html',context)
def image(request,width,height):
    return HttpResponse(generate(int(width), int(height)),content_type="image/png")