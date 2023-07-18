from django.shortcuts import render
def main(request):
    return render(request,'layout.html')

def home(request):
    return render(request,'home.html')