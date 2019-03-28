from django.shortcuts import render
from .forms import ContractForm
from django.http import HttpResponse


def contract(request):
    if request.method == "POST":
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contract/ok.html")
        else:
            return HttpResponse("Sorry")
    else:
        form = ContractForm()
        return render(request, "contract/contract.html", {"form": form})
