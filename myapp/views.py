from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CommentForm
from .models import Comment, Product, ProductType


def index(req):
    q = req.GET.get("search")
    if q == "":
        q = None
    types = ProductType.objects.all()
    products = Product.objects.order_by("type").distinct()
    comments = Comment.objects.all()
    return render(req, 'index.html', {'prod_types': types, 'products': products, 'comments': comments, 'search': q})


def make_comment(req):
    if req.method == 'POST':
        form = CommentForm(req.POST)
    if not form.is_valid():
        print(form.errors)
        return HttpResponse(status=400)
    Comment.objects.create(
        name=form.cleaned_data['name'], email=form.cleaned_data['email'], text=form.cleaned_data['text'])
    return redirect('/')
