# Generated by Django 3.1.7 on 2021-04-24 09:10

from django.db import migrations, models
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('about', models.CharField(blank='Write something about yourself in 140 characters.', max_length=140)),
            ],
        ),
    ]
