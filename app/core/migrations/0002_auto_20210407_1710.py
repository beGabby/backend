# Generated by Django 3.1.8 on 2021-04-07 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=1000),
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id_one', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_id_one', to=settings.AUTH_USER_MODEL)),
                ('user_ide_two', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_ide_two', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
