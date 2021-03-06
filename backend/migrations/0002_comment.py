# Generated by Django 3.0.7 on 2020-06-28 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250)),
                ('date', models.DateField(auto_now=True)),
                ('from_post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='from_post', to='backend.Post')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reply_set', to='backend.Comment')),
            ],
        ),
    ]
