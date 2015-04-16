# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waliki', '0005_auto_20141124_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InfoBox',
            fields=[
                ('block_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='waliki_blocks.Block')),
                ('content', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=('waliki_blocks.block',),
        ),
        migrations.AddField(
            model_name='block',
            name='page',
            field=models.ForeignKey(to='waliki.Page'),
            preserve_default=True,
        ),
    ]
