# Generated by Django 3.1.7 on 2021-06-23 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_accessorizing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Textile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='accessorizing',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='clothe',
            name='textiles',
            field=models.ManyToManyField(to='main_app.Textile'),
        ),
    ]
