# Generated by Django 2.2.9 on 2019-12-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='key',
            field=models.CharField(max_length=40),
        ),
    ]
