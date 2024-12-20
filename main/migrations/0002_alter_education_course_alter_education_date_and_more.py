# Generated by Django 5.1.4 on 2024-12-13 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='course',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='school',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='content1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='content2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='content3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='stack1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='stack10',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='stack2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='stack3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='stack4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='stack5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='stack6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='stack7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='stack8',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='stack9',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='subtitle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='content1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='content2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='content3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='duration',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='works/'),
        ),
        migrations.AlterField(
            model_name='work',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='stack1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='stack10',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='stack2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='stack3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='stack4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='stack5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='stack6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='stack7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='stack8',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='stack9',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='subtitle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
