from django import from .forms import

class TopicsForm(forms.Form):
    title_text = forms.CharField(max_length=30)
    content_text = forms.CharField(max_length=140)