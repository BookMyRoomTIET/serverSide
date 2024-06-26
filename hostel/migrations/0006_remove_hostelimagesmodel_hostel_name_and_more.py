# Generated by Django 4.0.2 on 2022-05-21 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0005_rename_hostel_id_hostelimagesmodel_hostel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostelimagesmodel',
            name='hostel_name',
        ),
        migrations.RemoveField(
            model_name='hostelimagesmodel',
            name='image_link',
        ),
        migrations.RemoveField(
            model_name='hostelinformationmodel',
            name='hostel_image',
        ),
        migrations.AddField(
            model_name='hostelimagesmodel',
            name='hostel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hostel.hostelinformationmodel'),
        ),
        migrations.AddField(
            model_name='hostelimagesmodel',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
