# Generated by Django 4.0 on 2021-12-19 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('cost', models.IntegerField(blank=True)),
            ],
        ),
    ]