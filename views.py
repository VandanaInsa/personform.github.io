from django.shortcuts import render

# Create your views here.
def personform(request):
    return render( request, 'app/a.html')
def c(request):
    return render( request, 'app/c.html')
