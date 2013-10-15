from django.db import models
from django. template.defaultfilters import slugify
from model_utils.models import TimeStampedModel

# Create your models here.
class Text(TimeStampedModel):
    mean_scored_text = models.TextField()
    top_n_scored_text = models.TextField()
    title = models.CharField(max_length=255, default='Text')
    slug = models.SlugField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    objects = models.Manager()

    # Set output format to unicode
    def __unicode__(self):
        return u'{0}'.format(self.title)

    # Save slug method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Text, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return("")