# Generated by Django 2.0 on 2017-12-31 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0011_phonepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonepic',
            name='back_image',
            field=models.ImageField(upload_to='phones/phonepics'),
        ),
        migrations.AlterField(
            model_name='phonepic',
            name='front_image',
            field=models.ImageField(upload_to='phones/phonepics'),
        ),
    ]
