from .models import Product

def products_show(product_id = None):
    if product_id:
        product = Product.objects.get(id = product_id)
        data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'stock': product.stock
        }
        return data
    products = Product.objects.values()
    return list(products)
