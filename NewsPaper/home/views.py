from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'Главная'
    return render(request, 'home/home.html', {'title': title,})