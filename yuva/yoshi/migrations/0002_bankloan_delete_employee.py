# Generated by Django 5.1.3 on 2024-12-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoshi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bankloan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accno', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('ifsc', models.CharField(max_length=20)),
                ('micr', models.IntegerField()),
                ('phno', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
