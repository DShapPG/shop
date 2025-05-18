from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from .products import products_show
from django.core import serializers
import json
@csrf_exempt
def product(request, pk = None):
    if request.method == 'POST':
        product = Product.objects.create(name=request.POST['name'], price=request.POST['price'],
                                         stock=request.POST['stock'], description=request.POST['description'])
        return HttpResponse('Done')
    if request.method == 'GET':
        if pk:
            try:
                return JsonResponse(products_show(pk), safe=False)
            except Exception as e:
                if 'does not exist' in str(e):
                    return JsonResponse({'error': str(e)}, safe=False, status=404)
                return JsonResponse({'error': str(e)}, safe=False, status=500)
        return JsonResponse(products_show(), safe=False)

    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            product = Product.objects.get(id = data.get("id"))
            product.name = data.get("name")
            product.price = data.get("price")
            product.stock = data.get("stock")
            product.description = data.get("description")
            product.save()
            return HttpResponse('Done')
        except Exception as e:
            return JsonResponse({'error': str(e)}, safe=False, status=500)

    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            product = Product.objects.get(id = data.get("id"))
            product.delete()
            return HttpResponse('Deleted')
        except Exception as e:
            return JsonResponse({'error': str(e)}, safe=False, status=500)





