# Generated by Django 3.0.6 on 2020-06-07 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accesses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.IntegerField(choices=[(1, 'Assertive'), (2, 'Passive-aggressive'), (3, 'Aggressive'), (4, 'Submissive'), (5, 'Manipulative'), (6, 'Romantic')])),
                ('send_to', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('access', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accesses.Access')),
            ],
        ),
    ]
