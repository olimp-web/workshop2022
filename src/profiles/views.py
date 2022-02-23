from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import ProfilePage

# Create your views here.


class IndexPageView(TemplateView):
    template_name = 'profiles/index.html'

    def get_context_data(self, **kwargs):
        return {
            "students": ProfilePage.objects.values('id', 'title')
        }


class ProfilePageView(TemplateView):
    template_name = 'profiles/profile.html'

    def get_context_data(self, profile_id, **kwargs):
        # try:
        profile = ProfilePage.objects.get(id=profile_id)
        # except ProfilePage.DoesNotExists():

        return {
            "profile": profile
        }
