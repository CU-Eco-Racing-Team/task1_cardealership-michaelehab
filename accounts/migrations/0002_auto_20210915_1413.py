# Generated by Django 3.2.7 on 2021-09-15 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='accounts.user'),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='dealer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dealer', to='accounts.user'),
        ),
        migrations.AlterField(
            model_name='industry',
            name='industry',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='industry', to='accounts.user'),
        ),
    ]
