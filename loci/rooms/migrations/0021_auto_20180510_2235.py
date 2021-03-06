# Generated by Django 2.0.3 on 2018-05-10 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0020_auto_20180510_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marquee_style',
            old_name='scrollamount',
            new_name='scrollamount_range',
        ),
        migrations.RenameField(
            model_name='marquee_style',
            old_name='scrolldelay',
            new_name='scrolldelay_range',
        ),
        migrations.AddField(
            model_name='marquee_style',
            name='cur_scrollamount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='marquee_style',
            name='cur_scrolldelay',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='words_style',
            name='color',
            field=models.CharField(blank=True, default='0,0,0', max_length=13),
        ),
    ]
