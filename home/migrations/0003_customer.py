# Generated by Django 3.0.6 on 2020-07-11 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200710_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.IntegerField(default=0)),
            ],
        ),
    ]
