from django.shortcuts import render

from .models import Blog
from .models import Fashion
from .models import Poetry


# a simple function that renders the index page with the multiple objects in a dict (context)
def index_view(request):
    blog_items = Blog.objects.all()
    fashion_items = Fashion.objects.all()
    poetry_items = Poetry.objects.all()

    context = {
        "blog_items": blog_items,
        "fashion_items": fashion_items,
        "poetry_items": poetry_items
    }

    return render(request, "blog/index.html", context)


def about_view(request):
    blog_items = Blog.objects.all()
    fashion_items = Fashion.objects.all()
    poetry_items = Poetry.objects.all()

    context = {
        "blog_items": blog_items,
        "fashion_items": fashion_items,
        "poetry_items": poetry_items
    }
    return render(request, "blog/about.html", context)


def fashion_view(request):
    blog_items = Blog.objects.all()
    fashion_items = Fashion.objects.all()
    poetry_items = Poetry.objects.all()

    context = {
        "blog_items": blog_items,
        "fashion_items": fashion_items,
        "poetry_items": poetry_items
    }

    return render(request, "blog/fashion.html", context)


def poetry_view(request):
    blog_items = Blog.objects.all()
    fashion_items = Fashion.objects.all()
    poetry_items = Poetry.objects.all()

    context = {
        "blog_items": blog_items,
        "fashion_items": fashion_items,
        "poetry_items": poetry_items
    }

    return render(request, "blog/poetry.html", context)


def contact_view(request):
    blog_items = Blog.objects.all()
    fashion_items = Fashion.objects.all()
    poetry_items = Poetry.objects.all()

    context = {
        "blog_items": blog_items,
        "fashion_items": fashion_items,
        "poetry_items": poetry_items
    }

    return render(request, "blog/contact.html", context)


def art_view(request):
    blog_items = Blog.objects.all()
    fashion_items = Fashion.objects.all()
    poetry_items = Poetry.objects.all()

    context = {
        "blog_items": blog_items,
        "fashion_items": fashion_items,
        "poetry_items": poetry_items
    }

    return render(request, "blog/art.html", context)
