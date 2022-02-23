# Generated by Django 4.0.1 on 2022-02-09 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'emp',
            },
        ),
    ]
