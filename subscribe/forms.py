from django import forms
from django.utils.translation import gettext_lazy as _

from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
  class Meta:
    model = Subscribe
    fields = '__all__'
    labels = {
      'first_name': _('Enter First Name'),
      'last_name': _('Enter Last Name')
    }
    

# class SubscribeForm(forms.Form):
#   first_name = forms.CharField(max_length=100)
#   last_name = forms.CharField(max_length=100)
#   email = forms.EmailField()

#   def clean_first_name(self):
#     data = self.cleaned_data['first_name']
#     if "," in data:
#       raise forms.ValidationError("Invalid First Name")
#     return data

