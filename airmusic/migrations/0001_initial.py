# Generated by Django 3.1.2 on 2021-06-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.TextField(blank=True)),
                ('parameters', models.TextField(blank=True)),
                ('use', models.TextField(blank=True)),
                ('color', models.TextField(blank=True)),
            ],
        ),
    ]