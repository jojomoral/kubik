# Generated by Django 4.0.3 on 2022-05-10 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0005_chat_users_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='users_id',
            field=models.CharField(default='[]', max_length=500),
        ),
    ]