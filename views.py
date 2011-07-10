# Create your views here.
from django.http import HttpResponse

#This view is used for the main altitude page ('/').
def index(request):
    return HttpResponse("Hello, world. You're at the index.")
