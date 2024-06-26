# Generated by Django 5.0.6 on 2024-05-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='more_details_for_the_dedicated_page',
            field=models.TextField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='paragraph',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
