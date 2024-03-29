# Generated by Django 3.0.6 on 2020-07-10 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField(default=0)),
                ('p_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=500)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('stock', models.IntegerField(default=0)),
                ('subcategory', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
