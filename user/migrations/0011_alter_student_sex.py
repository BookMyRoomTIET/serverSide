# Generated by Django 4.0.4 on 2022-05-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_student_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
