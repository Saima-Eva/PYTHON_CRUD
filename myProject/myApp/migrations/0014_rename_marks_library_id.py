# Generated by Django 4.2.7 on 2023-12-03 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_authority_marks_employees_marks_library_marks_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='library',
            old_name='Marks',
            new_name='ID',
        ),
    ]