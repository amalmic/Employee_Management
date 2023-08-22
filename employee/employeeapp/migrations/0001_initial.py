# Generated by Django 4.2.1 on 2023-06-14 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Employees',
                'db_table': 'dbdemo1_employee',
            },
        ),
    ]