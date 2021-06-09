# Generated by Django 3.1.2 on 2021-06-08 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airmusic', '0004_list_progress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='id',
        ),
        migrations.AlterField(
            model_name='list',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='p', serialize=False, to='airmusic.method'),
        ),
    ]
