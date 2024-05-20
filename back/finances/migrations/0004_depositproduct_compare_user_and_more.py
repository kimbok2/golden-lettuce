# Generated by Django 4.2.8 on 2024-05-20 00:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finances', '0003_depositproduct_join_user_savingproduct_join_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='depositproduct',
            name='compare_user',
            field=models.ManyToManyField(related_name='compare_deposit', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='savingproduct',
            name='compare_user',
            field=models.ManyToManyField(related_name='compare_saving', to=settings.AUTH_USER_MODEL),
        ),
    ]
