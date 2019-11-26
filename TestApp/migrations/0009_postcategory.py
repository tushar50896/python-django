# Generated by Django 2.2.6 on 2019-11-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0008_auto_20191124_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_category', models.CharField(max_length=200)),
                ('category_slug', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
