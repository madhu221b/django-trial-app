from rest_framework import serializers

from .models import Student, School, Book


class SchoolSerializer(serializers.ModelSerializer):
    school = serializers.CharField(read_only=True)

    class Meta:
        model = School


class BookSerializer(serializers.ModelSerializer):
    book = serializers.CharField(read_only=True)

    class Meta:
        model = Book


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    school_name = serializers.CharField(source='school.school', read_only=True)
    phone = serializers.CharField(source='school.phone', read_only=True)
    book_title = serializers.CharField(source='books.title', read_only=True)
    pages = serializers.CharField(source='books.no_of_pages', read_only=True)

    class Meta:
        model = Student
        fields = ('firstname', 'lastname', 'email', 'gender', 'school_name', 'phone', 'book_title', 'pages')
