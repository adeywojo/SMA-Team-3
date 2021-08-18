# Generated by Django 3.2.5 on 2021-08-17 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_user_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followers',
            name='follower_id',
        ),
        migrations.AddField(
            model_name='followers',
            name='follower_id',
            field=models.ForeignKey(default=2930, on_delete=django.db.models.deletion.CASCADE, related_name='follower_id', to='authentication.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='followers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follows_id', to=settings.AUTH_USER_MODEL),
        ),
    ]