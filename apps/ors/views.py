from django.shortcuts import render


# Create your views here.
def db_panel_view(request):
    return render(request, 'db_panel.html')
