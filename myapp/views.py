from myapp.forms import UserFormSet
from django.shortcuts import render


def manage_users(request):
    businessprofileid = 'g1'
    if request.method == 'POST':
        formset = UserFormSet(businessprofile_id=businessprofileid, data=request.POST)
        if formset.is_valid():
            formset.save()
            # do something
    else:
        formset = UserFormSet(businessprofile_id=businessprofileid)
    return render(request, "manage_users.html", {"formset": formset})
