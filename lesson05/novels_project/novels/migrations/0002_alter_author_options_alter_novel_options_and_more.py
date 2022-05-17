# Generated by Django 4.0.4 on 2022-05-17 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('name', 'bio', 'country'), 'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='novel',
            options={'ordering': ('title', 'description', 'author', 'original_title'), 'verbose_name': 'Новелла', 'verbose_name_plural': 'Новеллы'},
        ),
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='novels.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='description',
            field=models.TextField(blank=True, help_text='Описание', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='original_title',
            field=models.CharField(blank=True, help_text='Оригинальное название новеллы', max_length=128, null=True, verbose_name='Оригинальное название'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='title',
            field=models.CharField(blank=True, help_text='Название новеллы', max_length=128, null=True, verbose_name='Название'),
        ),
    ]