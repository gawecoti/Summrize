from django.views.generic import ListView, CreateView
from .models import Text
from .forms import TextForm
from text_summarize import *
from django.http import HttpResponseRedirect

class FeedView(ListView):
    model = Text
    template_name = 'feed.html'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.all().order_by('-date')

class TextAdd(CreateView):
    model = Text
    form_class = TextForm
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        summarized_text = summarize(form.data['text'],int(form.data['num_sentences']))
        self.object.mean_scored_text = summarized_text[0].encode('latin1','ignore')
        self.object.top_n_scored_text = summarized_text[1].encode('latin1','ignore')
        self.object.title = form.data['title']
        self.object.save()
        return HttpResponseRedirect('/text/')

    def form_invalid(self, form):
        print form.errors
        return HttpResponseRedirect('/')



