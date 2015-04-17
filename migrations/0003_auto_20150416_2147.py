# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waliki_blocks', '0002_auto_20150416_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infobox',
            options={'verbose_name': 'infobox', 'verbose_name_plural': 'infoboxes'},
        ),
        migrations.AlterModelOptions(
            name='infoboxentry',
            options={'verbose_name': 'entry', 'verbose_name_plural': 'entries'},
        ),
        migrations.AlterModelOptions(
            name='infoboxsection',
            options={'verbose_name': 'section', 'verbose_name_plural': 'sections'},
        ),
        migrations.AlterField(
            model_name='infoboxentry',
            name='section',
            field=models.ForeignKey(to='waliki_blocks.InfoBoxSection'),
        ),
    ]
