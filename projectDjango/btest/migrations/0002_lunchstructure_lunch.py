# Generated by Django 4.2.6 on 2023-10-23 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('btest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lunchstructure',
            name='lunch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='btest.lunch', verbose_name='Обед'),
        ),
    ]
