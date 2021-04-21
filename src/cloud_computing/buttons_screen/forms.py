from django import forms
from djng.forms import NgModelFormMixin
from djng.styling.bootstrap3.forms import Bootstrap3FormMixin

from buttons_screen.models import UploadedImages


class ButtonScreenForm(forms.ModelForm):
    class Meta:
        model = UploadedImages
        fields = ('image', )


class MetaDataScreenForm(Bootstrap3FormMixin, NgModelFormMixin, forms.Form):
    data = forms.CharField(widget=forms.HiddenInput(), required=False)
