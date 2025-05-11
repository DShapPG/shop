from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def products(request):
    if request.method == 'POST':
        return HttpResponse(request.POST.items())
    return HttpResponse('GET')

    # Create your views here.
