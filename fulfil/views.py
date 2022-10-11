from django.shortcuts import render


def home(request):
    # if request.method == 'POST':
    return render(request, 'index.html')
