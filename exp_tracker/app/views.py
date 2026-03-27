from django.shortcuts import render
from .models import Expense
# Create your views here.

def addForm(request):
    if request.method=='POST':  
        name=request.POST.get('name');
        amount=request.POST.get('amount');
        Expense.object.create(name=name,amount=amount) 
        return render(request,'index.html')
    return render(request,'form.html')


