# Generated by Django 2.0.3 on 2018-05-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0017_auto_20180510_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words_style',
            name='cur_color',
            field=models.CharField(blank=True, default='black', max_length=13),
        ),
    ]
