# Generated by Django 5.1.2 on 2024-11-04 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0002_investimento_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investimento',
            name='nivel',
        ),
    ]
