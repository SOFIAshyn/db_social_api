# Generated by Django 3.0.6 on 2020-06-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('users', '0003_auto_20200607_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ManyToManyField(blank=True, related_name='participants', to='groups.Group'),
        ),
    ]
