from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import DetailView
from datetime import timedelta, datetime
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
from .models import Settings, Slider
from services.models import (
    Product,
    Configuration,
    ConfigurationKeyPoint,
)




class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        settings_obj = Settings.objects.first()

        context["settings_obj"] = settings_obj
        context["slider"] = Slider.objects.all()
        context["product"] = Product.objects.all()
        context["configuration"] = Configuration.objects.all()
        context["configuration_key_point"] = ConfigurationKeyPoint.objects.all()

        return context