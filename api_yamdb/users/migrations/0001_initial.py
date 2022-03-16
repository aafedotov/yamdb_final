# Generated by Django 2.2.16 on 2022-02-09 11:04

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=150, unique=True, validators=[users.validators.validate_username], verbose_name='имя пользователя')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='последний вход в систему')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Администратор')),
                ('is_active', models.BooleanField(default=True, verbose_name='активный')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Суперпользователь')),
                ('role', models.CharField(choices=[('user', 'Аутентифицированный пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='user', max_length=64, verbose_name='role')),
                ('bio', models.TextField(blank=True, verbose_name='о себе')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='имя')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='фамилия')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]