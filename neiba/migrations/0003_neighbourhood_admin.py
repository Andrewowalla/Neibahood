# Generated by Django 4.0.3 on 2022-03-20 14:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neiba', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='neiba.profile'),
            preserve_default=False,
        ),
    ]