# Generated by Django 4.0.2 on 2022-03-01 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Course name', max_length=200)),
                ('duration', models.BigIntegerField(help_text='Coure Duration')),
                ('description', models.TextField(help_text='Course Description')),
                ('image', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='tell you opinion')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Topic Name', max_length=200)),
                ('description', models.TextField(help_text='Topic Description')),
                ('duration', models.CharField(help_text='Topic Duration', max_length=100)),
                ('video', models.FileField(help_text='video/', upload_to='')),
                ('article', models.TextField(help_text='Topic Article')),
                ('likes', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.course')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Reply for discussion')),
                ('discussion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.discussion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.topic')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='Question', max_length=200)),
                ('answer', models.CharField(help_text='Answer', max_length=200)),
                ('option1', models.CharField(help_text='option 1', max_length=200)),
                ('option2', models.CharField(help_text='option 2', max_length=200)),
                ('option3', models.CharField(help_text='option 3', max_length=200)),
                ('option4', models.CharField(help_text='option 4', max_length=200)),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.topic')),
            ],
        ),
        migrations.AddField(
            model_name='discussion',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.topic'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]