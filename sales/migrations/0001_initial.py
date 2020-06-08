# Generated by Django 3.0.6 on 2020-06-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField()),
                ('duration', models.IntegerField(choices=[(1, 'One Day'), (7, 'Week')])),
            ],
        ),
    ]
