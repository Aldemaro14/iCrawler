# Generated by Django 3.1.2 on 2020-10-19 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201019_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrapyitem',
            old_name='description',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='scrapyitem',
            name='deliveryDate',
        ),
        migrations.RemoveField(
            model_name='scrapyitem',
            name='pictures',
        ),
        migrations.RemoveField(
            model_name='scrapyitem',
            name='price',
        ),
        migrations.RemoveField(
            model_name='scrapyitem',
            name='title',
        ),
    ]
