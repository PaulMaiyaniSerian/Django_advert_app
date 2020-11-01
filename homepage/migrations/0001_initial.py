# Generated by Django 3.0 on 2020-07-20 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('time', models.CharField(max_length=200)),
                ('comments', models.TextField()),
            ],
        ),
    ]
