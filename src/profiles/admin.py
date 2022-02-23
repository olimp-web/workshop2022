from django.contrib import admin
from django.forms import ModelForm, CharField
from django_ace import AceWidget

from .models import ProfilePage

# Register your models here.


class ProfilePageForm(ModelForm):
    content = CharField(widget=AceWidget(mode='html', theme='twilight'))

    class Meta:
        fields = ('title', 'content', 'id')


@admin.register(ProfilePage)
class ProfilePageAdmin(admin.ModelAdmin):
    form = ProfilePageForm
