# Generated by Django 4.0.2 on 2022-02-14 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Star rating', 'verbose_name_plural': 'Stars rating'},
        ),
    ]
