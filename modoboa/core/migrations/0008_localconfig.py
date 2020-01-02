# Generated by Django 1.9.5 on 2016-06-15 18:12
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('core', '0007_auto_20151116_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_pk', models.PositiveIntegerField(null=True)),
                ('api_versions', jsonfield.fields.JSONField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
        ),
    ]
