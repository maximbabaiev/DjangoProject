# Generated by Django 4.1.3 on 2022-12-16 17:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.IntegerField(default=0, validators=[django.core.validators.MaxLengthValidator(5), django.core.validators.MinLengthValidator(1)])),
                ('financing', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinLengthValidator(0)])),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('severity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=13, null=True, validators=[django.core.validators.RegexValidator('r^+380\\d{9}$')])),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinLengthValidator(0.01)])),
                ('premium', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinLengthValidator(0)])),
                ('surname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayOfWeek', models.PositiveIntegerField(default=1, verbose_name=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(7)])),
                ('endTime', models.TimeField()),
                ('name', models.CharField(max_length=100, unique=True)),
                ('startTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.IntegerField(validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(5)])),
                ('floor', models.IntegerField(validators=[django.core.validators.MinLengthValidator(1)])),
                ('name', models.CharField(max_length=30, unique=True)),
                ('places', models.IntegerField(verbose_name=[django.core.validators.MinLengthValidator(1)])),
                ('departmentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson_10_Models.department')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinLengthValidator(0.01)])),
                ('date', models.DateField(auto_now=True)),
                ('departmentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson_10_Models.department')),
                ('sponsorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson_10_Models.sponsor')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorsExamination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endTime', models.TimeField()),
                ('startTime', models.TimeField()),
                ('doctorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson_10_Models.doctor')),
                ('examinationId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson_10_Models.examination')),
                ('wardId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson_10_Models.ward')),
            ],
        ),
    ]
