# Generated by Django 5.0.1 on 2024-01-21 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0002_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='from_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course', to='studies.course', verbose_name='ссылка на курс'),
        ),
    ]
