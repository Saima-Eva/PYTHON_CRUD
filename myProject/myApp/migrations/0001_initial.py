# Generated by Django 4.2.7 on 2023-11-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
            ],
        ),
    ]
