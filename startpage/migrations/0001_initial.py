# Generated by Django 4.0.3 on 2022-04-05 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('invite_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('birth', models.DateField(auto_now=True)),
                ('online', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('text', models.TextField(max_length=4096)),
                ('is_read', models.BooleanField(default=False)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startpage.chat')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startpage.user')),
            ],
        ),
    ]