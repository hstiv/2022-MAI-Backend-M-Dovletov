# Generated by Django 4.0.4 on 2022-05-15 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Название новеллы', max_length=128, null=True)),
                ('original_title', models.CharField(blank=True, help_text='Оригинальное название новеллы', max_length=128, null=True)),
                ('description', models.TextField(blank=True, help_text='Описание', null=True)),
                ('author', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novels.author')),
            ],
        ),
    ]