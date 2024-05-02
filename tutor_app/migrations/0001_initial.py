# Generated by Django 4.2.11 on 2024-05-01 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('custom_id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(null=True)),
                ('phone', models.CharField(max_length=20)),
                ('user_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('lesson_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tutor_app.customuser')),
                ('education_level', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('tutor_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tutor_app.customuser')),
                ('education_level', models.CharField(max_length=100)),
                ('brief_info', models.CharField(max_length=255)),
                ('educational_institution', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('payment_status', models.CharField(max_length=100)),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_app.lesson')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_app.subject'),
        ),
        migrations.CreateModel(
            name='TutorSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_app.subject')),
                ('tutor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_app.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='StudentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_app.subject')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_app.lesson')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_app.student')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='tutor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_app.tutor'),
        ),
    ]
