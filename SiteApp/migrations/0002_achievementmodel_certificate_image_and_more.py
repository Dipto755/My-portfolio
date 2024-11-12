# Generated by Django 5.1.3 on 2024-11-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievementmodel',
            name='certificate_image',
            field=models.ImageField(default='', upload_to='media/achievements/'),
        ),
        migrations.AddField(
            model_name='certificationmodel',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='certificationmodel',
            name='image',
            field=models.ImageField(default='', upload_to='media/certification/'),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='certificate_image',
            field=models.ImageField(default='', upload_to='media/experience/'),
        ),
    ]