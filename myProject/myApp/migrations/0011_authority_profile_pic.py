# Generated by Django 4.2.7 on 2023-11-26 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_employees_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='media/profile_pic'),
        ),
    ]
