# Generated by Django 3.1.7 on 2021-03-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbconnectivity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=30)),
            ],
        ),
    ]