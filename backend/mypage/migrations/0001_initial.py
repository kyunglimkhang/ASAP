# Generated by Django 3.2.3 on 2021-05-31 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recommend', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.FloatField()),
                ('items', models.ManyToManyField(related_name='orders', to='recommend.Item')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_history', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]