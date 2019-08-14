from django.conf import settings
from django.db import models
from django.utils import timezone


class Files(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField(upload_to='fles')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	def __str__(self):
		return self.title


    
