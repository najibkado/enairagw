# Generated by Django 3.0.8 on 2022-08-05 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_paymentattempt_paymentsettlement'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentattempt',
            name='added',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='paymentattempt',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.00, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentattempt',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='paymentattempt',
            name='status',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentattempt',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='payment', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wallet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL),
        ),
    ]
