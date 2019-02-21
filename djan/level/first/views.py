from django.shortcuts import render
from django.http import HttpResponse
from first.models import AccessRecord, Webpage, Topic
# Create your views here.

def index(request):
    acc = AccessRecord.objects.order_by('date')
    my_dict = {'ins': acc}
    return render(request, 'index.html', context=my_dict)