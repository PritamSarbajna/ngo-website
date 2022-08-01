# Generated by Django 4.0.6 on 2022-07-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'contacts',
            },
        ),
    ]
