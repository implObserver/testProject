# Generated by Django 4.0.3 on 2022-03-23 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_urls_url_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url',
            options={'ordering': ['-created_at'], 'verbose_name': 'Доступные ссылки', 'verbose_name_plural': 'Доступные ссылки'},
        ),
    ]
