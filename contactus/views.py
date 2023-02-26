from django.shortcuts import render , redirect
from django.views.generic import TemplateView , FormView
from django.urls import reverse_lazy , reverse
from .form import ContactForm
from .models import ContactUsModels , Contacts
from mixins import LoginRequirdMixins , LogoutRequirdMixins


class ContactUs(LogoutRequirdMixins , FormView):
    template_name = 'contactus/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home:main')
    def form_valid(self, form):
        cd = form.cleaned_data
        ContactUsModels.objects.create(username=cd['username'] , email=cd['email'] , phone_number=cd['phone_number'] , subject = cd['subject'] , message = cd['message'] , is_Accept_terms = cd['is_Accept_terms'])
        return redirect(reverse_lazy('home:main'))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.all()
        return context