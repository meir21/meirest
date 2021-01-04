from main.models import Branch, Topping, Dish


def branches(request):
    return {
        'branches': Branch.objects.all()
    }


def dishes(request):
    return {
        'dish': Dish.objects.first()
    }


def toppings(request):
    return {
        'toppings': Topping.objects.all()
    }