# Generated by Django 4.0.6 on 2022-07-12 13:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('boleto', '0002_remove_boleto_valor_boleto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleto',
            name='id_boleto',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
