# Generated by Django 2.2.1 on 2019-05-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0006_auto_20190529_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='type',
            field=models.CharField(blank=True, choices=[('поиск', 'Партнер'), ('идеи', 'Идеи'), ('работа', 'Работа')], max_length=100),
        ),
    ]
