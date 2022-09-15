# Generated by Django 3.2.10 on 2022-09-15 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymodels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='object_id',
        ),
        migrations.AddField(
            model_name='item',
            name='data',
            field=models.JSONField(default=''),
            preserve_default=False,
        ),
    ]