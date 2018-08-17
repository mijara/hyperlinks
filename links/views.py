from django.urls import reverse_lazy
from django.views import generic

from links.models import Link
from links.forms import LinkUpdateForm


class LinkUpdateView(generic.UpdateView):
    model = Link
    form_class = LinkUpdateForm

    success_url = reverse_lazy('landing:main')


class LinkDeleteView(generic.DeleteView):
    model = Link

    success_url = reverse_lazy('landing:main')
