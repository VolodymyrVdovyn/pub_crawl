# Generated by Django 3.1.4 on 2020-12-16 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punishments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='punishment',
            options={'verbose_name': 'Покарання', 'verbose_name_plural': 'Покарання'},
        ),
        migrations.AddField(
            model_name='level',
            name='url',
            field=models.SlugField(max_length=130, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='punishment',
            name='url',
            field=models.SlugField(max_length=130, null=True, unique=True),
        ),
    ]