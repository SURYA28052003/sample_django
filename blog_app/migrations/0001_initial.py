# Generated by Django 5.0 on 2023-12-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(default='surya', editable=False, max_length=200)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(max_length=5000)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
