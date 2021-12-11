from django.shortcuts import render

from .models import Comment, Product, ProductType


def index(req):
    q = req.GET.get("search")
    if q == "":
        q = None
    types = ProductType.objects.all()
    products = Product.objects.order_by("type").distinct()
    comments = Comment.objects.all()
    return render(req, 'index.html', {'prod_types': types, 'products': products, 'comments': comments, 'search': q})
