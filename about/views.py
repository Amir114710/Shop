from django.shortcuts import render
from django.views.generic import TemplateView
from about.models import AboutModel, PosterAbout, PropertyShop


class AboutView(TemplateView):
    template_name = 'about/about.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['about'] = AboutModel.objects.all()
        context['poster_about'] = PosterAbout.objects.all()
        context['PropertyShop'] = PropertyShop.objects.all()
        return context
