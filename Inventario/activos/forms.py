# activos/forms.py

from django import forms

class UploadFileForm(forms.Form):
    archivo_csv = forms.FileField()
