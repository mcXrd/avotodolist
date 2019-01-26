# Generated by Django 2.1.5 on 2019-01-26 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('label', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.Task')),
            ],
        ),
    ]
