from django.shortcuts import render
from .models import CertificateVs
from django.db.models import Q
from django.http import HttpResponse


def getvs(request):
    q = request.GET.get('a')
    p = request.GET.get('b')

    if q and p:
        result1 = CertificateVs.objects.filter(Q(cert_name__contains=q)).first()
        result2 = CertificateVs.objects.filter(Q(cert_name__contains=p)).first()
        if result1 and result2:
            return render(request, 'certvs/vs.html', {'result1': result1, 'result2': result2})
        else:
            return HttpResponse('fail')
    else:
        return render(request, 'certvs/vs.html')


