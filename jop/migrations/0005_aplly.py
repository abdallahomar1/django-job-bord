# Generated by Django 3.1.1 on 2020-09-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0004_auto_20200918_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=99)),
                ('website', models.URLField()),
                ('cover_letter', models.TextField(max_length=500)),
            ],
        ),
    ]