# Generated by Django 4.2.4 on 2023-09-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="date",
            field=models.DateField(default="2001-02-08"),
            preserve_default=False,
        ),
    ]
