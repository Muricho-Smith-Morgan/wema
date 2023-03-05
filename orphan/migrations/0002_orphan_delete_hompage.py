# Generated by Django 4.1.6 on 2023-02-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orphan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=30)),
                ('guardian', models.CharField(max_length=50)),
                ('education_status', models.CharField(max_length=50)),
                ('current_donor', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Hompage',
        ),
    ]