from django.urls import reverse_lazy
from django.views import generic
from links.models import Link
from links.forms import LinkForm


class MainView(generic.CreateView):
    model = Link
    form_class = LinkForm

    template_name = 'landing/main.html'

    success_url = reverse_lazy('landing:main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['link_list'] = Link.objects.all()

        return context
