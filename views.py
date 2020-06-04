from django.http import *
from django.shortcuts import *

def index(request):
    return render(request, 'index.html')
    return HttpResponse("hello")

def dis(request):

    scp1 = request.GET.get('scp', 'default')
    bcp1 = request.GET.get('bcp', 'default')
    param = {"t1": scp1, "t2": bcp1}

    if 1 <= int(scp1) <= 12 and 1 <= int(bcp1) <= 12:
        if int(bcp1) == 12:
            param.update({"finaltime": scp1+':00'})
        else:
            param.update({"finaltime": scp1+':'+str(int(bcp1)*5)})
    else:
        return HttpResponse('Enter the valid data')

    return render(request, 'dis.html', param)










