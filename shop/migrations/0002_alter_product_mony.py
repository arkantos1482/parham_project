# Generated by Django 4.0.6 on 2022-08-04 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mony',
            field=models.CharField(choices=[('dollers', '$'), ('تومان', 'تومان')], default='dollers', max_length=10),
        ),
    ]
