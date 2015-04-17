# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waliki_blocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoBoxEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=60)),
                ('text', models.CharField(max_length=100)),
                ('link', models.URLField(null=True, blank=True)),
                ('section', models.ForeignKey(to='waliki_blocks.InfoBox')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InfoBoxSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('infobox', models.ForeignKey(to='waliki_blocks.InfoBox')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='infobox',
            name='content',
        ),
        migrations.AddField(
            model_name='infobox',
            name='caption',
            field=models.CharField(max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='infobox',
            name='image',
            field=models.ImageField(null=True, upload_to=b'blocks/images', blank=True),
            preserve_default=True,
        ),
    ]
