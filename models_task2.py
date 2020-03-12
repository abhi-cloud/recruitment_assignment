# DevCom Rcruitment assignment
# THINK task 2 of backend assignment

from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Author(models.Model):

	id = models.UUIDField(primary_key = True, default = uuid4, editable = False, ) 
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name


class Book(models.Model):

	id = models.UUIDField(primary_key = True, default = uuid4, editable = false)
	time_of_addition = models.DateTimeField(default = timezone.now)

	isbn = models.CharField(max_length = 13)
	title = models.CharField(max_length = 50)
	short_description = models.TextField()

	owner = models.ForeignKey(
		User, on_delete = models.CASCADE, blank = False)

	#author also has reference to Author model
	author = models.ForeignKey(
		Author, default = None, on_delete = models.SET_DEFAULT, blank = True)

	current_rentee = models.ForeignKey(
		User, default = None, on_delete = models.SET_DEFAULT, blank = True)


	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Book"
		verbose_name_plural = "Books"
		ordering = ("title",)




class AuthorBookRelation(models.Model):

	id = models.UUIDField(primary_key = True, default = uuid4, editable = False, )

	author = models.ForeignKey(
		Author, on_delete = models.CASCADE, default = uuid4)
	book = models.ForeignKey(
		Book, on_delete = models.CASCADE, default= uuid4)

	def __str__(self):
		return self.author.name + " --> " + self.book.title


	class Meta:
		verbose_name = "Author-Book Relation"
		verbose_name_plural = "Author-Book Relations"
		ordering = ("author_name",)