from django.contrib import admin
from .models import Book, School, Student
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'date_of_publication', 'no_of_pages')


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school', 'email', 'principal', 'phone', 'address2')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'gender', 'school', 'books')


admin.site.register(Book, BookAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)