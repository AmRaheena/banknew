from django.shortcuts import render, get_object_or_404

from bankApp.models import Branch,Sub_branch


# Create your views here.



def allBranches(request,b_slug=None):

    br = None
    sub_list = None
    if b_slug != None:
        br = get_object_or_404(Branch, slug=b_slug)
        sub_list = Sub_branch.objects.all().filter(branch=br)
    return render(request, "branches.html", {'branch': br,'sub_list':sub_list})

def sub_branches(request,b_slug,sub_br_slug):
    try:
        sub_br = Sub_branch.objects.all().filter(branch__slug=b_slug,slug=sub_br_slug)

    except Exception as e:
        raise e
    return render(request,"details.html",{'sub_br':sub_br})