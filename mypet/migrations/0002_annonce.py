# Generated by Django 4.2 on 2023-05-25 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_animal', models.CharField(max_length=255)),
                ('espece', models.CharField(max_length=255)),
                ('race', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('image1', models.ImageField(upload_to='static/images/')),
                ('image2', models.ImageField(upload_to='static/images/')),
                ('image3', models.ImageField(upload_to='static/images/')),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('unknown', 'Unknown')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]