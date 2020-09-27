from django.shortcuts import render

# Create your views here.
def send_masseg(request):
     return render(request, 'contact/contact.html', {})