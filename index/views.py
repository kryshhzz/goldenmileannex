from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

from django.http import HttpResponse, Http404
from django.conf import settings
import os


def download_brochure_view(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'brochure.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def index_view(request):
    cont = {
        'kmi_form' : keep_me_interested_form,
        'e_form' : enquiry_form,
        'pav_form' : plan_a_visit_form,
    }
    if request.method == 'POST':
        tier = ''
        tier = request.POST.get('tier')
        if tier == '1':
            form = keep_me_interested_form(request.POST)
            if form.is_valid():
                obj = keep_me_interested.objects.create(
                    name = form.cleaned_data['name'],
                    email = form.cleaned_data['email'],
                    phone_number = form.cleaned_data['phone_number'],
                )
                obj.save()
                cont['message'] = 'You will be informed from now about Golden Mile Annex !'
        if tier == '2':
            form = enquiry_form(request.POST)
            if form.is_valid():
                obj = enquiry.objects.create(
                    name = form.cleaned_data['name'],
                    email = form.cleaned_data['email'],
                    phone_number = form.cleaned_data['phone_number'],
                    message = form.cleaned_data['message'],
                )
                obj.save()
                cont['message'] = 'We have received your message, we will get back to you soon.'
        if tier == '3':
            form = plan_a_visit_form(request.POST)
            if form.is_valid():
                obj = plan_a_visit.objects.create(
                    name = form.cleaned_data['name'],
                    email = form.cleaned_data['email'],
                    phone_number = form.cleaned_data['phone_number'],
                    preferred_date = form.cleaned_data['preferred_date'],
                    preferred_time = form.cleaned_data['preferred_time'],
                )
                obj.save()
                cont['message'] = 'We have received your request to make a visit to Golden Mile Annex, we will get back to you soon.'

    return render(request,'index.html',cont)

