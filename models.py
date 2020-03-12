# DevCom Rcruitment assignment
# THINK task 1 of backend assignment

from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Book(models.Model):

	id = models.UUIDField(primary_key = True, default = uuid4, editable = false)
	time_of_addition = models.DateTimeField(default = timezone.now)

	isbn = models.CharField(max_length = 13)
	title = models.CharField(max_length = 50)
	author = models.CharField(max_length = 50)
	short_description = models.TextField()


	# here i have setup one to many relationship  between users and books, in both
	# owner as well as current_rentee field
	# users model is automatically defined in django, and is initiated after some migration commands
	# users will be added to User model after SignUp   

	owner = models.ForeignKey(
		User, on_delete = models.CASCADE, blank = False)

	current_rentee = models.ForeignKey(
		User, default = None, on_delete = models.SET_DEFAULT, blank = True)


	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Book"
		verbose_name_plural = "Books"
		ordering = ("title",)