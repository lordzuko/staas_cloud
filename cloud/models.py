from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

def upload_file(instance, filename):
	return 'user_{0}/{1}'.format(instance.user.id, filename)

class Uploads(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	upload_file = models.FileField(upload_to=upload_file)
	uploaded_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'uploads'
