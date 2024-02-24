from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Comment
from .forms import CommentForm  # Assume you have a corresponding form for comments


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category_detail.html', {'category': category, 'products': products})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = Comment.objects.filter(product=product, is_active=True)
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.product = product
            comment.author = request.user
            comment.is_active = False  # Comments are inactive by default until approved
            comment.save()
            return redirect('product_detail', product_id=product.id)
    else:
        comment_form = CommentForm()

    return render(request, 'store/product_detail.html', {'product': product, 'comments': comments, 'comment_form': comment_form})
