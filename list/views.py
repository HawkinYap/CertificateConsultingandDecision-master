from django.shortcuts import render, get_object_or_404
from .models import CertificateTbl
from django.db.models import Q


def cert_list(request):
    lists = CertificateTbl.objects.all()
    return render(request, "list/list.html", {"lists": lists})

def cert_result(request, result_id):
    result = CertificateTbl.objects.get(cert_id=result_id)
    return render(request, "list/content.html", {"result":result})

def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = 'please enter what you want to check'
        return render(request, 'list/errors.html', {'error_msg': error_msg})
    result = CertificateTbl.objects.filter(Q(cert_name__contains=q) | Q(cert_ename__icontains=q)).first()
    if not result:
        return render(request, 'list/errors.html', {'error_msg': error_msg})
    return render(request, 'list/content.html', {'result': result})