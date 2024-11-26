# Generated by Django 5.1.2 on 2024-11-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='photo',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=200, verbose_name='descripcion'),
        ),
    ]