# Generated by Django 3.0.8 on 2022-08-05 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment_Attempt',
        ),
        migrations.DeleteModel(
            name='Payment_Settlement',
        ),
    ]