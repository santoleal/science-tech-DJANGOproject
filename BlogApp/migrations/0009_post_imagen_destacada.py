# Generated by Django 5.0.1 on 2024-02-03 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0008_rename_destacado_post_principal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen_destacada',
            field=models.ImageField(blank=True, null=True, upload_to='img_destacadas'),
        ),
    ]