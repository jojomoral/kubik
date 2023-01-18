# Generated by Django 4.0.3 on 2022-05-09 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('startpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='message_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='chat',
            name='creator_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='startpage.user'),
        ),
        migrations.AddField(
            model_name='user',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='startpage.chat'),
        ),
        migrations.AlterField(
            model_name='message',
            name='from_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='startpage.user'),
        ),
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
