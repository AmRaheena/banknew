from django.shortcuts import render, redirect

from accounts.models import Account


# Create your views here.
def create_account(request):
    if request.method == 'POST':
        name=request.POST.get('name',)
        dob = request.POST.get('dob', )
        age = request.POST.get('age', )
        gender = request.POST.get('gender', )
        ph_no = request.POST.get('ph_no', )
        mail_id = request.POST.get('mail_id', )
        address = request.POST.get('address', )
        district = request.POST.get('address', )
        branch = request.POST.get('branch', )
        ac_type = request.POST.get('ac_type', )
        materials = request.POST.get('materials', )
        account=Account(name=name,dob=dob,age=age,gender=gender,ph_no=ph_no,mail_id=mail_id,address=address,district=district,branch=branch,ac_type=ac_type,materials=materials)
        account.save()
        return redirect('credentials:login')
    return render(request, "account.html")

def details(request):
    return render(request,"details.html")






