from django.shortcuts import render
from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = "home_app/index.html"
