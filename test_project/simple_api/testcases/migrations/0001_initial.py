# Generated by Django 3.0.7 on 2020-09-22 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ASDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xy', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TestModelFKTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_field', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TestModelM2MTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_field', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TestModelPrimitiveFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_field', models.IntegerField()),
                ('float_field', models.FloatField()),
                ('string_char_field', models.CharField(max_length=50)),
                ('string_text_field', models.TextField()),
                ('bool_field', models.BooleanField()),
                ('date_field', models.DateField()),
                ('time_field', models.TimeField()),
                ('date_time_field', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TestModelM2MSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m2m_field', models.ManyToManyField(related_name='m2m_sources', to='testcases.TestModelM2MTarget')),
            ],
        ),
        migrations.CreateModel(
            name='TestModelFKSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_sources', to='testcases.TestModelFKTarget')),
                ('one_to_one_field', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testcases.TestModelFKTarget')),
            ],
        ),
    ]