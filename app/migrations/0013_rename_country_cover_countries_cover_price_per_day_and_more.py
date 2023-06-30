# Generated by Django 4.1 on 2022-08-19 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_cover_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cover',
            old_name='country',
            new_name='countries',
        ),
        migrations.AddField(
            model_name='cover',
            name='price_per_day',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9999),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CoverDetail',
        ),
    ]