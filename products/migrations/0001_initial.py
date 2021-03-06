# Generated by Django 3.1.3 on 2020-11-09 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Interactive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('bundle', models.FileField(blank=True, null=True, upload_to='bundles/')),
                ('data', models.JSONField(blank=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interactives', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('file', models.FileField(blank=True, null=True, upload_to='assets/')),
                ('meta', models.JSONField(blank=True, null=True)),
                ('interactive', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='products.interactive')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
