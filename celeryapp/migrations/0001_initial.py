# Generated by Django 4.1.1 on 2022-10-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CeleryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, max_length=50, null=True)),
                ('count', models.CharField(blank=True, max_length=10, null=True)),
                ('task_id', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
