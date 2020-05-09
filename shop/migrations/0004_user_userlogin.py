# Generated by Django 3.0.3 on 2020-04-17 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(default='', max_length=50)),
                ('user_phone', models.CharField(default='', max_length=20)),
                ('user_add1', models.CharField(default='', max_length=100)),
                ('user_add2', models.CharField(default='', max_length=100)),
                ('user_city', models.CharField(default='', max_length=20)),
                ('user_state', models.CharField(default='', max_length=20)),
                ('user_pincode', models.CharField(default='', max_length=10)),
                ('user_email', models.CharField(default='', max_length=80)),
                ('user_pass', models.CharField(default='', max_length=50)),
                ('user_sq1', models.CharField(default='', max_length=50)),
                ('user_sq1ans', models.CharField(default='', max_length=50)),
                ('user_sq2', models.CharField(default='', max_length=50)),
                ('user_sq2ans', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(default='', max_length=80)),
                ('user_pass', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
