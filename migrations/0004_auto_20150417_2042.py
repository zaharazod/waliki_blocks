# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waliki_blocks', '0003_auto_20150416_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quip', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuipBox',
            fields=[
                ('block_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='waliki_blocks.Block')),
            ],
            options={
                'abstract': False,
            },
            bases=('waliki_blocks.block',),
        ),
        migrations.AddField(
            model_name='quip',
            name='quipbox',
            field=models.ForeignKey(to='waliki_blocks.QuipBox'),
            preserve_default=True,
        ),
    ]
