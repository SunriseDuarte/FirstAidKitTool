from django.shortcuts import render, redirect, get_object_or_404
#from .forms import PostCreateForm, CommentForm
from .models import Location, Boxtyp, Boxitem, Inventur, Inventuritem
from .forms import LocationForm, BoxtypForm, BoxitemForm, InventuritemForm
from django.http import HttpResponse

def index(request):
    locations = Location.objects.all
    inventur = Inventur.objects.order_by('-created_at')
    return render(request, 'inventur/index.html', {'locations': locations, 'inventurs': inventur})

def dataadmin(request):
    locations = Location.objects.all
    boxtyps = Boxtyp.objects.all
    boxitems = Boxitem.objects.all
    return render(request, 'inventur/admin.html', {'locations': locations, 'boxtyps': boxtyps, 'items': boxitems})


def startinventur(request, loc_id):
    location = get_object_or_404(Location, id=loc_id)
    inv_obj = Inventur(inv_name=location.loc_name, inv_location=location, created_by=request.user.username)
    inv_obj.save() #hier wird es gespeichert!!! Ändern zu erst nach knopf druck speichern?

    for item in location.boxtyp.boxitems.all():
        inv_item_obj = Inventuritem(inv_id=inv_obj, inv_name=item.item_name, item_amount_soll=item.item_amount, item_amount_ist=0, inv_comment="no comment")
        inv_item_obj.save()#hier auch

    #inventuritems = Inventuritem.objects.filter(inv_id=inv_obj)
    return redirect('inventur', inv_id=inv_obj.pk)

def inventur(request, inv_id):
    inv_obj = get_object_or_404(Inventur, pk=inv_id)
    inventuritems = Inventuritem.objects.filter(inv_id=inv_obj)
    allForms = []

    for inv_item in inventuritems:
        allForms.append(InventuritemForm(instance=inv_item))

    return render(request, 'inventur/inventur.html', {'inventur': inv_obj, 'inventuritems': inventuritems, 'forms':allForms})


def boxtyp_data(request, box_id):
    item = get_object_or_404(Boxtyp, pk=box_id)
    form = BoxtypForm(request.POST or None, instance=item)

    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            return redirect('dataadmin')
    else:
        form = BoxtypForm(instance=get_object_or_404(Boxtyp, pk=box_id))

    return render(request, 'inventur/boxtyp.html', {'form': form, 'item':item})

def location_data(request, loc_id):
    if request.method == 'POST':
        if loc_id > 0:
            item = get_object_or_404(Location, pk=loc_id)
            form = LocationForm(request.POST or None, instance=item)
        else:
            form = LocationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dataadmin')

    if 'new' in request.GET:
        form = LocationForm(request.POST or None)
        return render(request, 'inventur/location.html', {'form': form})
    
    location = get_object_or_404(Location, pk=loc_id)
    form = LocationForm(instance=location)    

    return render(request, 'inventur/location.html', {'form': form, 'location':location})

def item_data(request, item_id):
    if request.method == 'POST':
        if item_id > 0:
            item = get_object_or_404(Boxitem, pk=item_id)
            form = BoxitemForm(request.POST or None, instance=item)
        else:
            form = BoxitemForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('dataadmin')

    if 'new' in request.GET:
        form = BoxitemForm(request.POST or None)
        return render(request, 'inventur/boxitem.html', {'form': form})
    
    item = get_object_or_404(Boxitem, pk=item_id)
    form = BoxitemForm(instance=item)    

    return render(request, 'inventur/boxitem.html', {'form': form, 'item':item})

def updateinvitem(request):
    #for key, value in request.POST.items():
    #    print('Key: %s' % (key) ) 
    # print(f'Key: {key}') in Python >= 3.7
    #    print('Value %s' % (value) )
    # print(f'Value: {value}') in Python >= 3.7
    
    inv_id = request.POST.get('inv_id')
    inv_item = get_object_or_404(Inventuritem, pk=inv_id)
    #form = InventuritemForm(instance=inv_item)
    print(inv_item.inv_name)
    #form = InventuritemForm(request.POST or None, instance=inv_item)
    #print (form)
    inv_item.item_amount_ist = request.POST.get('id_item_amount_ist')
    inv_item.inv_comment = request.POST.get('id_inv_comment')
    inv_item.save()

    return HttpResponse("Alles OK")