# Generated by Django 4.2.4 on 2023-08-19 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Website_Title', models.CharField(blank=True, max_length=1000)),
                ('Date', models.DateField(blank=True)),
            ],
        ),
    ]
