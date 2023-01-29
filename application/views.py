from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request,'application/gallery.html')

def viewPhoto(request):
    return render(request,'application/photo.html')

def addPhoto(request):
    return render(request,'application/add.html')