# Generated by Django 4.2.7 on 2023-11-26 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_alter_authority_age_alter_authority_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='myImage',
            field=models.ImageField(null=True, upload_to='media/profile_pic'),
        ),
    ]