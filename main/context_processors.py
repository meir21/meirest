from main.models import Branch, Topping, Dish


def branches(request):
    return {
        'branches': Branch.objects.all()
    }


