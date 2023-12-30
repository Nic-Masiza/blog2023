# Generated by Django 3.2.11 on 2023-12-29 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_remove_blog_full_content_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('tech', 'Tech'), ('sports', 'Sports'), ('politics', 'Politics'), ('adventure', 'Adventure')], default='tech', max_length=20),
        ),
    ]
