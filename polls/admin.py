from django.contrib import admin
from .models import Question, Person, Blocks, Book

# Register your models here.
admin.site.register(Question)
admin.site.register(Person)
admin.site.register(Blocks)
admin.site.register(Book)