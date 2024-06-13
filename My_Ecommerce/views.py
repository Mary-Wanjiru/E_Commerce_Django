from django.shortcuts import render
from .models import Products

# Create your views here.
def product_list(request):
    products = Products.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'My_Ecommerce/product_list.html',context)


from django.shortcuts import render

def index(request):
    # Your view logic goes here
    return render(request, 'index.html')  # Assuming you have an HTML template named index.html
