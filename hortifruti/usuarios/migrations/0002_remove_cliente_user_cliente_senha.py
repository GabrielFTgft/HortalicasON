# Generated by Django 5.1.3 on 2024-12-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='user',
        ),
        migrations.AddField(
            model_name='cliente',
            name='senha',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
