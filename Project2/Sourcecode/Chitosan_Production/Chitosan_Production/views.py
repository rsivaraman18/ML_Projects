from django.shortcuts import render

def home_view(request):
    return render(request, 'Base_Main_Page/Home_Page.html')