# Generated by Django 4.2.8 on 2023-12-23 13:41

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'اجرا',
            },
        ),
        migrations.CreateModel(
            name='Sans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('capacity', models.IntegerField()),
                ('free_capacity', models.IntegerField()),
                ('min_ticket', models.IntegerField()),
                ('max_ticket', models.IntegerField()),
                ('start_sale_date', django_jalali.db.models.jDateTimeField()),
                ('end_sale_date', django_jalali.db.models.jDateTimeField()),
                ('datetime', django_jalali.db.models.jDateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.event')),
            ],
            options={
                'verbose_name': 'سانس',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticketid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('sans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.sans')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
            options={
                'verbose_name': 'بلیط',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('rooydad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
            options={
                'verbose_name': 'نظرات',
            },
        ),
    ]
