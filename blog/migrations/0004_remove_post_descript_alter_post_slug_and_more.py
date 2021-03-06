# Generated by Django 4.0.4 on 2022-05-13 03:11

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='descript',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipes', to='blog.post'),
        ),
    ]
