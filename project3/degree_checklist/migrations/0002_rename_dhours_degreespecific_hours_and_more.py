# Generated by Django 4.2.5 on 2023-10-08 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('degree_checklist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='degreespecific',
            old_name='dhours',
            new_name='hours',
        ),
        migrations.RenameField(
            model_name='degreespecific',
            old_name='dSubject_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='degreespecific',
            name='dclasses_offered',
        ),
    ]