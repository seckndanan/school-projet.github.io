# Generated by Django 3.1.14 on 2022-01-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20220129_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicinfo',
            name='previous_academic_info',
        ),
        migrations.RemoveField(
            model_name='studentaddressinfo',
            name='union',
        ),
        migrations.RemoveField(
            model_name='studentaddressinfo',
            name='upazilla',
        ),
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=910504, unique=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='nationality',
            field=models.CharField(choices=[('Senegalais', 'Senegalaise'), ('Others', 'Others')], max_length=45),
        ),
        migrations.DeleteModel(
            name='PreviousAcademicInfo',
        ),
    ]
