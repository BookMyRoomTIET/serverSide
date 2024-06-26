# Generated by Django 4.0.2 on 2022-05-20 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hostelAllocatedToYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradYear', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('hostel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel.hostelinformationmodel')),
            ],
        ),
    ]
