# Generated by Django 4.0.3 on 2022-05-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0009_remove_profile_last_seen_remove_profile_online'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
