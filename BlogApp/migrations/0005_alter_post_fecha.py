# Generated by Django 5.0.1 on 2024-02-03 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0004_alter_post_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
