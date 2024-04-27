from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'POST':
        data={
            'key':request.POST['keyword']
            }
    else:
        data={
            'key' : 'asdsa'
        }
    return render(request , 'index.html' , {"data":data})