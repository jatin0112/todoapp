# Generated by Django 4.0.3 on 2022-03-15 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reminderthings',
            options={'verbose_name': 'reminder thingss', 'verbose_name_plural': 'reminder Things'},
        ),
        migrations.RenameField(
            model_name='reminderthings',
            old_name='name',
            new_name='title',
        ),
    ]
