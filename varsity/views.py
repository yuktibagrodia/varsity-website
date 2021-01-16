from django.shortcuts import render, redirect

def home(request):
    return render(request, "Home_page.html")
    pass
def members(request):
    return render(request,"Members.html")
    pass
def gallery(request):
    return render(request,"gallery.html")
    pass
def collaboration(request):
    return render(request,"collaborations.html")
    pass