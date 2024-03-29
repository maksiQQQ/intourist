# Generated by Django 4.0.4 on 2022-04-15 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('B', 'Bishkek'), ('C', 'Chuy'), ('I', 'Issyk-Kul'), ('N', 'Naryn'), ('T', 'Talas'), ('O', 'Osh'), ('D', 'Djala-Abad'), ('A', 'Batken')], max_length=1)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile_photo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
