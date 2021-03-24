# Generated by Django 3.1.7 on 2021-03-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210323_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='btn_txt',
            field=models.TextField(blank=True, null=True, verbose_name='عنوان دکمه'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='postcat', to='blog.Category', verbose_name='دسته بندی'),
        ),
    ]
