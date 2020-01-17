# Generated by Django 3.0.2 on 2020-01-17 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0022_delete_classregistration'),
        ('academic', '0004_classregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.PersonalInfo')),
            ],
        ),
        migrations.AlterField(
            model_name='classregistration',
            name='guide_teacher',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.GuideTeacher'),
        ),
    ]
