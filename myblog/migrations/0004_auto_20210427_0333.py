# Generated by Django 3.2 on 2021-04-27 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_alter_comment_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='body',
        ),
    ]
