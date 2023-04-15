# Generated by Django 4.2 on 2023-04-15 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('body', models.TextField(blank=True)),
                ('gameID', models.IntegerField()),
                ('replies', models.IntegerField()),
            ],
        ),
    ]
