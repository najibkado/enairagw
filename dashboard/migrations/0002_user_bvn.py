# Generated by Django 3.0.8 on 2022-08-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bvn',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
