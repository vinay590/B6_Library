from django.http import HttpResponse

def view_a(request):
    return HttpResponse('view_a')

def view_b(request):
    return HttpResponse('view_b')