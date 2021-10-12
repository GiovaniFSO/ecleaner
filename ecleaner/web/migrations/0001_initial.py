# Generated by Django 3.2.8 on 2021-10-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=12, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('street', models.CharField(max_length=60)),
                ('number', models.IntegerField()),
                ('neighborhood', models.CharField(max_length=30)),
                ('complement', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('code', models.IntegerField()),
                ('profile_picture', models.ImageField(upload_to='')),
            ],
        ),
    ]