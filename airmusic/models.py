from django.contrib.auth.models import AbstractUser
from django.db import models


class color(models.Model):
	col=models.CharField(max_length=128)
	def __str__(self):
		return self.col

class method(models.Model):
	function = models.TextField(blank=True)
	parameters = models.TextField(blank=True)
	use = models.TextField(blank=True)
	json = models.TextField(blank=True, default="This is empty, please add something")
	color=models.ForeignKey(color,on_delete=models.CASCADE,related_name="c")
	code = models.TextField(blank=True, default="No code here :(")
	def __str__(self):
		return self.function

class list(models.Model):
	post=models.ForeignKey(method,on_delete=models.CASCADE,related_name="p", primary_key=True)
	progress = models.TextField(blank=True,default="Oops! this is empty")
	