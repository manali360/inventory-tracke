from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Category,Item


# Create your views here.
@login_required
def add_item(request):
    categories=Category.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        category=request.POST.get('category')
        quantity=request.POST.get('quantity')
        description=request.POST.get('description')
        category=Category.objects.get(id=category)
        item=Item.objects.create(user=request.user,name=name,category=category,quantity=quantity,description=description)
        item.save()
    return render(request,'add_inventory.html',{'categories':categories})

@login_required
def edit_item(request,*args,**kwargs):
    id=kwargs.get('id')
    item=Item.objects.filter(id=id).first()
    categories=Category.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        category=request.POST.get('category')
        quantity=request.POST.get('quantity')
        description=request.POST.get('description')
        item.name=name
        item.category=category
        item.quantity=quantity
        item.description=description
        item.save()
    return render(request,'add_inventory.html',{'item':item,'categories':categories})

    

@login_required
def del_item(request,id):
    item=Item.objects.get(id=id)
    item.delete()
    return redirect('inventory_view')

@login_required
def view_invt(request):
    items=Item.objects.filter(user=request.user).order_by('-created_at')  
    return render(request,'inventory_view.html',{'items':items})