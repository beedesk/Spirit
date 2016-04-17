# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trusts', '0001_initial'),
        ('spirit_category', '0003_category_is_global'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title', 'pk'], 'default_permissions': ('add', 'change', 'delete', 'read', 'add_topic_to'), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='trust',
            field=models.ForeignKey(related_name='spirit_category_category_content', default=1, to='trusts.Trust'),
        ),
    ]
