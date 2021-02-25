from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.

def home(request):
    object_form = ObjectForm()
    pdata = None
    if request.method == 'POST':
        object_form = ObjectForm()
        h1 = request.POST.get('Handle_1')
        h2 = request.POST.get('Handle_2')
        h3 = request.POST.get('Handle_3')
        print(h1, h2, h3)

        Odata = Object.objects.get(Handle_1=h1, Handle_2=h2, Handle_3=h3)
        # print(Odata)
        pdata = Odata.param_set.all()
        # print(Odata, pdata, "Hello World-1111111", sep='\n \n')
        # for i in pdata:
        #     print(i.ParamValue)
    context = {'object_form': object_form, 'pdata': pdata}
    return render(request, 'app_server/home_page.html', context=context)
