# Generated by Django 5.0.3 on 2024-03-18 20:52

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Оценка')),
                ('date_add', models.DateField(auto_now_add=True, null=True, verbose_name='Дата добавления')),
                ('date_upd', models.DateField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('date', models.DateField(null=True, verbose_name='Дата оценки')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scool.course', verbose_name='Курс')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='scool.person', verbose_name='Чья оценка')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
    ]
