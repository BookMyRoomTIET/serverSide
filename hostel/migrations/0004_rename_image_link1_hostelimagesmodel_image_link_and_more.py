# Generated by Django 4.0.2 on 2022-05-21 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0003_remove_hostelimagesmodel_hostel_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostelimagesmodel',
            old_name='image_link1',
            new_name='image_link',
        ),
        migrations.RemoveField(
            model_name='hostelimagesmodel',
            name='image_link10',
        ),
        migrations.RemoveField(
            model_name='hostelimagesmodel',
            name='image_link2',
        ),
        migrations.RemoveField(
            model_name='hostelimagesmodel',
            name='image_link3',
        ),
        migrations.RemoveField(
            model_name='hostelimagesmodel',
            name='image_link4',
        ),
        migrations.RemoveField(
            model_name='hostelimagesmodel',
            name='image_link5',
        ),
        migrations.RemoveField(
            model_name='hostelimagesmodel',
            name='image_link6',
        ),
        migrations.RemoveField(
            model_name='hostelimagesmodel',
            name='image_link7',
        ),
        migrations.RemoveField(
            model_name='hostelimagesmodel',
            name='image_link8',
        ),
        migrations.RemoveField(
            model_name='hostelimagesmodel',
            name='image_link9',
        ),
        migrations.AddField(
            model_name='hostelimagesmodel',
            name='hostel_id',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.RemoveField(
            model_name='hostelinformationmodel',
            name='hostel_image',
        ),
        migrations.AddField(
            model_name='hostelinformationmodel',
            name='hostel_image',
            field=models.ManyToManyField(blank=True, null=True, to='hostel.hostelImagesModel'),
        ),
    ]
