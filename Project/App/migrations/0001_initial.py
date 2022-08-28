# Generated by Django 4.1 on 2022-08-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mobile', models.BigIntegerField(default=0)),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
    ]
