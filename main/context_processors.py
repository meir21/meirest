from main.models import Branch

def branches(request):
    return {
        'branches' : Branch.objects.all()
    }