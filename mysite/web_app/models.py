from django.db import models


class School(models.Model):
    school = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    principal = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)

    def __str__(self):
        return self.school


class Book(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    date_of_publication = models.CharField(max_length=200)
    no_of_pages = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Student(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)


# b = Book(title="Sands of Iwo Jima", author_name="Philippine Hinemoor", date_of_publication="20-11-2017", no_of_pages=812)
