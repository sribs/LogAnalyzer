# Generated by Django 2.1.5 on 2019-01-19 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perf_log_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Perf_log_<django.db.models.fields.related_descriptors.ForwardManyToOneDescriptor object at 0x7f527e420dd8>_<django.db.models.query_utils.DeferredAttribute object at 0x7f527e420e48>.png', models.ImageField(unique=True, upload_to='')),
                ('log_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Log_template')),
            ],
        ),
    ]
