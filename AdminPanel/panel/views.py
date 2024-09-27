from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Partner
from .forms import PartnerForm, EditPartnerForm

class AdminLoginView(LoginView):
    template_name = 'admin_login.html'


@login_required
def dashboard(request):
    partners = Partner.objects.all() 
    total_partners = partners.count()  
    recent_activity = "No recent activity." 

    context = {
        'partners': partners,
        'total_partners': total_partners,
        'recent_activity': recent_activity,
    }
    return render(request, 'dashboard.html', context)



@login_required
def partner_list(request):
    partners = Partner.objects.all()
    return render(request, 'partner_list.html', {'partners': partners})




@login_required
def add_partner(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PartnerForm()
    return render(request, 'add_partner.html', {'form': form})



@login_required
def partner_details(request, partner_id):
    partner = get_object_or_404(Partner, id=partner_id)
    return render(request, 'partner_details.html', {'partner': partner})



@login_required
def edit_partner(request, partner_id):
    partner = get_object_or_404(Partner, id=partner_id)
    if request.method == 'POST':
        form = EditPartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PartnerForm(instance=partner)
    return render(request, 'edit_partner.html', {'form': form, 'partner': partner})

