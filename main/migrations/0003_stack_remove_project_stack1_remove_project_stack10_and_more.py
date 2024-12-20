# Generated by Django 5.1.4 on 2024-12-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_education_course_alter_education_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='stacks/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='stack1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='stack10',
        ),
        migrations.RemoveField(
            model_name='project',
            name='stack2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='stack3',
        ),
        migrations.RemoveField(
            model_name='project',
            name='stack4',
        ),
        migrations.RemoveField(
            model_name='project',
            name='stack5',
        ),
        migrations.RemoveField(
            model_name='project',
            name='stack6',
        ),
        migrations.RemoveField(
            model_name='project',
            name='stack7',
        ),
        migrations.RemoveField(
            model_name='project',
            name='stack8',
        ),
        migrations.RemoveField(
            model_name='project',
            name='stack9',
        ),
        migrations.RemoveField(
            model_name='work',
            name='stack1',
        ),
        migrations.RemoveField(
            model_name='work',
            name='stack10',
        ),
        migrations.RemoveField(
            model_name='work',
            name='stack2',
        ),
        migrations.RemoveField(
            model_name='work',
            name='stack3',
        ),
        migrations.RemoveField(
            model_name='work',
            name='stack4',
        ),
        migrations.RemoveField(
            model_name='work',
            name='stack5',
        ),
        migrations.RemoveField(
            model_name='work',
            name='stack6',
        ),
        migrations.RemoveField(
            model_name='work',
            name='stack7',
        ),
        migrations.RemoveField(
            model_name='work',
            name='stack8',
        ),
        migrations.RemoveField(
            model_name='work',
            name='stack9',
        ),
        migrations.AddField(
            model_name='project',
            name='stacks',
            field=models.ManyToManyField(blank=True, related_name='projects', to='main.stack'),
        ),
        migrations.AddField(
            model_name='work',
            name='stacks',
            field=models.ManyToManyField(blank=True, related_name='works', to='main.stack'),
        ),
    ]
