# Generated by Django 3.1.7 on 2021-03-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210323_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='postcat', to='blog.Category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='post',
            name='short_description',
            field=models.TextField(null=True, verbose_name='توضیحات کوتاه'),
        ),
    ]
