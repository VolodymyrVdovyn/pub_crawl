# Generated by Django 3.1.4 on 2020-12-16 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('punishments', '0003_auto_20201216_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='punishment',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='punishments.level', verbose_name='Рівень складності'),
        ),
    ]
