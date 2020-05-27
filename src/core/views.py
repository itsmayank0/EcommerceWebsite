from django.shortcuts import render
from .models import Items


def item_list(request):
    context = {
        'items': Items.objects.all()
    }
    return render(request,'home-page.html', context)

# python manage.py 