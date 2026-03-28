from django.shortcuts import render,redirect,get_object_or_404
from .models import Expense
# Create your views here.

def addForm(request):
    if request.method=='POST':  
        name=request.POST.get('name');
        amount=request.POST.get('amount');
        Expense.objects.create(name=name,amount=amount) 
        return render(request,'index.html')
    return render(request,'form.html')


def listExp(request):
    exp=Expense.objects.all()
    return render(request,'list.html',{'expenses':exp})

def deleteExp(request,id):
    exp=get_object_or_404(Expense,id=id)
    exp.delete()
    return render(request,'index.html')

def updateExp(request, id):
    exp = get_object_or_404(Expense, id=id)

    if request.method == 'POST':
        exp.name = request.POST.get('name')
        exp.amount = request.POST.get('amount')
        exp.save()

        return render(request,'index.html')   # ✅ better

    return render(request, 'edit.html', {'exp': exp})



