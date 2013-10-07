from django.views.generic import ListView, CreateView
from .models import Text
from .forms import TextForm
from text_summarize import *
from django.http import HttpResponseRedirect

class FeedView(ListView):
    model = Text
    template_name = 'feed.html'

    def get_queryset(self):
        return self.model.objects.all()

class TextAdd(CreateView):
    model = Text
    form_class = TextForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        summarized_text = summarize(form.data['text'])
        self.object.text = summarized_text
        self.object.save()
        return HttpResponseRedirect('/text/')



