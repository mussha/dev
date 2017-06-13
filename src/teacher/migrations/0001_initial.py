# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 10:57
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import teacher.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('variables', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(blank=True, max_length=20, null=True)),
                ('title', models.CharField(max_length=120)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('contact', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: 'XXXXXXX'.", regex='^\\d{8}$')])),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True)),
                ('years_of_experience', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('group_tuition', models.BooleanField(default=False)),
                ('website_url', models.CharField(blank=True, max_length=60, null=True)),
                ('salary_expectation', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('salary_negotiable', models.BooleanField(default=False)),
                ('postal_code', models.CharField(blank=True, max_length=6, null=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('docs_verified', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to=teacher.models.image_upload_to)),
                ('doc1', models.ImageField(blank=True, null=True, upload_to=teacher.models.doc_upload_to1)),
                ('doc2', models.ImageField(blank=True, null=True, upload_to=teacher.models.doc_upload_to2)),
                ('doc3', models.ImageField(blank=True, null=True, upload_to=teacher.models.doc_upload_to3)),
                ('doc4', models.ImageField(blank=True, null=True, upload_to=teacher.models.doc_upload_to4)),
                ('doc5', models.ImageField(blank=True, null=True, upload_to=teacher.models.doc_upload_to5)),
                ('doc6', models.ImageField(blank=True, null=True, upload_to=teacher.models.doc_upload_to6)),
                ('education', models.ManyToManyField(to='variables.Education')),
                ('education_school', models.ManyToManyField(to='variables.Education_School')),
                ('educational_level', models.ManyToManyField(to='variables.Educational_Level')),
                ('expertise_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='variables.Expertise_Type')),
                ('first_level', models.ManyToManyField(to='variables.Level_Expertise')),
                ('first_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='variables.Subject_Expertise')),
                ('region', models.ManyToManyField(to='variables.Region')),
                ('second_level', models.ManyToManyField(related_name='level2', to='variables.Level_Expertise')),
                ('second_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject2', to='variables.Subject_Expertise')),
                ('third_level', models.ManyToManyField(related_name='level3', to='variables.Level_Expertise')),
                ('third_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject3', to='variables.Subject_Expertise')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
