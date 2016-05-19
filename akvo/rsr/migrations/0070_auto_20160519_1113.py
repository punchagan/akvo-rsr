# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import akvo.rsr.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rsr', '0069_auto_20160517_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='sector_code',
            field=akvo.rsr.fields.ValidXMLCharField(help_text='It is possible to specify a variety of sector codes, based on the selected vocabulary. The sector codes for the DAC-5 and DAC-3 vocabularies can be found here: <a href="http://iatistandard.org/202/codelists/Sector/" target="_blank">DAC-5 sector codes</a> and <a href="http://iatistandard.org/202/codelists/SectorCategory/" target="_blank">DAC-3 sector codes</a>.', max_length=25, verbose_name='sector code', blank=True),
            preserve_default=True,
        ),
    ]
