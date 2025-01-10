from django.shortcuts import render,HttpResponse

# Create your views here.
def test(request):
    text = "<h1>Hey!...hi!...Goois</h1>"
    return HttpResponse(text)

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')