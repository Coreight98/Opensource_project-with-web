# Generated by Django 3.2.3 on 2021-05-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('form', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('todo', 'Todo'), ('done', 'Done')], default='todo', max_length=10)),
            ],
        ),
    ]
