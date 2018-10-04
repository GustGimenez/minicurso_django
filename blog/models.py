from django.db import models
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField(verbose_name='Titulo')
	author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
	created_data = models.DateTimeField(default=timezone.now)
	publish_date = models.DateTimeField(blank=True, null=True)


	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	
	# Sobreescrevendo o método de python
	def __str__(self):
		return '{} - {}'.format(self.title, self.author)