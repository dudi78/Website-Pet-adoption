# Generated by Django 4.2 on 2023-05-20 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypet', '0006_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('ad_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_complet', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=20)),
                ('animal_name', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=8)),
                ('race', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypet.user')),
            ],
        ),
    ]