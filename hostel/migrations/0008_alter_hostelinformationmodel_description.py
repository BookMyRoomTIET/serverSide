# Generated by Django 4.0.4 on 2022-05-22 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0007_hostelpreferencefirstyear_hostelpreferencesecondyear_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelinformationmodel',
            name='description',
            field=models.CharField(max_length=10000),
        ),
    ]