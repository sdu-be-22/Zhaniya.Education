# Generated by Django 4.0.4 on 2022-05-23 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_video_classes_alter_video_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Pan')),
                ('authors', models.TextField(verbose_name='Avtorlary')),
                ('front_image', models.ImageField(blank=True, null=True, upload_to='book_images')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
            },
        ),
    ]
