# Generated by Django 3.1.1 on 2020-12-16 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mectworkplace', '0002_tutor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutor',
            old_name='staffid',
            new_name='staff',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='studentid',
            new_name='student',
        ),
    ]
