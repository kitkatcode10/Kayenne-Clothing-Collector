# Generated by Django 3.1.7 on 2021-06-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('size', models.CharField(max_length=100)),
            ],
        ),
    ]


# monitor this, because you dumbass named your model CAT and now you manually changed it 