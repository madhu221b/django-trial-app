# Generated by Django 3.1.7 on 2021-03-16 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author_name', models.CharField(max_length=200)),
                ('date_of_publication', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('principal', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.book')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.school')),
            ],
        ),
    ]
