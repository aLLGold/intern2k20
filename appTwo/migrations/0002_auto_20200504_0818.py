# Generated by Django 3.0.5 on 2020-05-04 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=264, unique=True),
        ),
    ]