from django import forms

from links import services
from .models import Link


class LinkForm(forms.ModelForm):
    def save(self, commit=True):
        meta = services.link_metadata(self.cleaned_data['url'])

        self.instance.title = meta['title']

        if meta['keywords'] is not None:
            self.instance.keywords = meta['keywords'].lower()

        if meta['description'] is not None:
            self.instance.description = meta['description']

        return super().save(commit)

    class Meta:
        model = Link
        fields = ('url',)


class LinkUpdateForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('title', 'keywords', 'description')
