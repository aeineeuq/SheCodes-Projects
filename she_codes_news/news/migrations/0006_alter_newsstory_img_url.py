# Generated by Django 3.2.5 on 2021-08-27 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20210825_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='img_url',
            field=models.URLField(default='https://picsum.photos/600', max_length=250),
        ),
    ]
