from django.shortcuts import render
from .forms import *
from .models import *
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .forms import *

# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def home(request):
    object_form = ObjectForm()
    pdata = None
    # cache.clear()
    if request.method == 'POST':
        object_form = ObjectForm()
        h1 = request.POST.get('Handle_1')
        h2 = request.POST.get('Handle_2')
        h3 = request.POST.get('Handle_3')
        print(h1, h2, h3)
        h123 = str(h1) + str(h2) + str(h3)
        if cache.get(h123):
            print("DATA COMING FROM CACHE")
            Odata = cache.get(h123)
            print(Odata)
            # print(Odata[0])
        else:
            Odata = Object.objects.get(Handle_1=h1, Handle_2=h2, Handle_3=h3)
            print("DATA COMING FROM DB")
            print(Odata)
            # cache.set_many({h1:Odata,h2:Odata,h3:Odata})
            h123 = str(h1) + str(h2) + str(h3)
            cache.set(h123, Odata)
            print(cache.get(h123))
        # print(Odata)
        # pdata = Odata.param_set.all()
        # if cache.get(Odata):
        #     pdata  = cache.get(Odata)
        #     print("DATA COMING FROM CACHE pdata")
        # else:
        #     pdata = Odata.param_set.all()
        #     cache.set_many({Odata:pdata})
        #     print(cache.get(Odata))
        #     print("DATA COMING FROM DB pdata")
        # print(Odata, pdata, "Hello World-1111111", sep='\n \n')
        # for i in pdata:
        #     print(i.ParamValue)
    context = {'object_form': object_form, 'pdata': pdata}
    return render(request, 'app_server/home_page.html', context=context)


def view_object(request):
    # cache.clear()
    form = form_object()
    handle_values = None
    handles = None
    if request.method == "POST":
        oid = request.POST.get('ObjectID')
        if cache.get(oid):
            print("DATA COMING FROM CACHE")
            handles = cache.get(oid)
            handle_values = cache.get(handles)
            print(handles)
        else:
            handles = Object.objects.get(ObjectID=oid)
            handle_values = str(handles.Handle_1) + " " + str(handles.Handle_2) + " " + str(handles.Handle_3)
            print("DATA COMING FROM DB")
            cache.set(oid, handles)
            cache.set(handles, handle_values)
            print(handles)
            print(handles.Handle_1)
    # handles.ObjectRevision +=handles.ObjectRevision
    # print("The objectRevision is",handles.ObjectRevision)
    context = {'form': form, 'handle_values': handle_values, 'handles': handles}
    return render(request, 'app_server/object.html', context)
