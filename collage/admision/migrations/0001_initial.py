# Generated by Django 4.1.4 on 2023-09-06 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('cours', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
            ],
        ),
    ]
