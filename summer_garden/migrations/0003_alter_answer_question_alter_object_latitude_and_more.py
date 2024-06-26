# Generated by Django 4.2.11 on 2024-05-15 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('summer_garden', '0002_alter_answer_options_alter_answer_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='summer_garden.question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='object',
            name='latitude',
            field=models.CharField(max_length=100, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='object',
            name='longitude',
            field=models.CharField(max_length=100, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='objectimage',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='summer_garden.object', verbose_name='Объект'),
        ),
        migrations.AlterField(
            model_name='question',
            name='image_base64',
            field=models.TextField(blank=True, verbose_name='base64 кодировка фотографии'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='summer_garden.quiz', verbose_name='Викторина'),
        ),
    ]
