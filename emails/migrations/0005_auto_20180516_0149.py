# Generated by Django 2.0 on 2018-05-15 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0004_emailcampaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcampaign',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lists.List'),
        ),
    ]
