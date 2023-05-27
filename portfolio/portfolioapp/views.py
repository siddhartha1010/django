# from django.shortcuts import render
# from portfolioapp.models import Form
# from django.views.generic import (TemplateView,View)

# # Create your views here.
# def my_view(request):
#     form = Form()
#     return render(request, 'head.html', {'form': form})
from django.shortcuts import render

from .forms import MyForm

def my_form(request):
    form = MyForm()
    if request.method =="POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
       
    return render(request, 'index.html', {'form': form})


