# Generated by Django 3.1.6 on 2021-02-13 09:03

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='web',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('date', models.DateField()),
                ('department', models.CharField(max_length=40)),
                ('doctor', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=150)),
            ],
        ),
    ]
