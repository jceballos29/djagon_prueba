# Generated by Django 2.2.24 on 2021-10-27 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('activa', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField()),
                ('cantidad_publicaciones', models.IntegerField()),
            ],
        ),
    ]
