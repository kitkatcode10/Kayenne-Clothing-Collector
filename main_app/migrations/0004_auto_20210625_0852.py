# Generated by Django 3.1.7 on 2021-06-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210623_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessorizing',
            name='date',
            field=models.DateField(verbose_name='accessorizing date'),
        ),
    ]
