# Generated by Django 3.2.5 on 2021-08-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='famous_ghazals',
            fields=[
                ('ghazal_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('tags', models.CharField(max_length=500)),
                ('writer', models.CharField(max_length=100)),
                ('shayari', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ghazals_home',
            fields=[
                ('ghazal_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('tags', models.CharField(max_length=500)),
                ('writer', models.CharField(max_length=100)),
                ('shayari', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='new_ghazals',
            fields=[
                ('ghazal_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('tags', models.CharField(max_length=500)),
                ('writer', models.CharField(max_length=100)),
                ('shayari', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('verification_status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]