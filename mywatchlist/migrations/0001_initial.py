# Generated by Django 4.1 on 2022-09-16 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWatchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField()),
                ('title', models.CharField(max_length=255)),
                ('rating', models.FloatField(max_length=5)),
                ('release_date', models.DateField()),
                ('review', models.TextField()),
            ],
        ),
    ]
