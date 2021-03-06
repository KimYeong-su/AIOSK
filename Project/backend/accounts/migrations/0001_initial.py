# Generated by Django 2.2.16 on 2020-11-10 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNum', models.CharField(max_length=20)),
                ('point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]
