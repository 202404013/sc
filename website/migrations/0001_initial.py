# Generated by Django 5.1.4 on 2024-12-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('nickname', models.CharField(max_length=50)),
                ('insta', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('song', models.CharField(max_length=50)),
                ('music_video', models.CharField(max_length=50)),
                ('time_stamp', models.CharField(max_length=50)),
                ('theory', models.CharField(max_length=5000)),
            ],
        ),
    ]
