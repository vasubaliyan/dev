# Generated by Django 4.1.7 on 2023-03-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('subcategory_name', models.CharField(default=None, max_length=10, null=True)),
                ('subcategory_description', models.CharField(default=None, max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
