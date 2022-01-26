# Generated by Django 4.0.1 on 2022-01-25 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lohsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('money', models.CharField(max_length=100)),
                ('payment', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('date', models.DateField()),
            ],
        ),
    ]