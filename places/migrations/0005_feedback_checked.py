# Generated by Django 4.0.4 on 2022-05-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='checked',
            field=models.BooleanField(default=False, verbose_name='Обработано'),
        ),
    ]
