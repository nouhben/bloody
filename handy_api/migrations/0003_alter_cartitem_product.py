# Generated by Django 4.0.4 on 2022-05-24 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handy_api', '0002_productimage_alter_handyuser_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='handy_api.product'),
        ),
    ]
