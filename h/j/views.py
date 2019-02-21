from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, 'index.html')

def form_name(request):
    form = forms.formname()

    if request.method == 'POST':
        form = forms.formname(request.POST)

        if form.is_valid():
            print("validation success")
            print("NAME:" + form.cleaned_data['name'])
            print("EMAIL:" + form.cleaned_data['email'])
            print("PASSWORD:" + form.cleaned_data['text'])
    return render(request, 'form.html', {'form': form})
