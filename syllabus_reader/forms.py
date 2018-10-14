from django import forms
from datetime import datetime


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def handle_uploaded_file(f):
    date_str = datetime.now()
    date_str = date_str.strftime('%Y%m%d-%H:%M:%S')
    f_str = '/media/%s_file.pdf' % date_str
    with open(f_str, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return f_str
