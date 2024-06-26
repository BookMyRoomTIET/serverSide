# Generated by Django 4.0.2 on 2022-05-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0006_remove_hostelimagesmodel_hostel_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='hostelPreferenceFirstYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollNumber', models.IntegerField()),
                ('cgpa', models.FloatField()),
                ('preferenceOne', models.CharField(max_length=100)),
                ('preferenceTwo', models.CharField(max_length=100)),
                ('preferenceThree', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='hostelPreferenceSecondYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollNumber', models.IntegerField()),
                ('cgpa', models.FloatField()),
                ('preferenceOne', models.CharField(max_length=100)),
                ('preferenceTwo', models.CharField(max_length=100)),
                ('preferenceThree', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='hostelmapmodel',
            old_name='map_link1',
            new_name='mapLink',
        ),
        migrations.RemoveField(
            model_name='hostelmapmodel',
            name='map_link2',
        ),
        migrations.RemoveField(
            model_name='hostelmapmodel',
            name='map_link3',
        ),
        migrations.RemoveField(
            model_name='hostelmapmodel',
            name='map_link4',
        ),
        migrations.RemoveField(
            model_name='hostelmapmodel',
            name='map_link5',
        ),
        migrations.AlterField(
            model_name='hostelinformationmodel',
            name='hostel_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
