# Generated by Django 3.2.20 on 2023-08-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=200, unique=True, verbose_name='Юзернейм'),
        ),
    ]
