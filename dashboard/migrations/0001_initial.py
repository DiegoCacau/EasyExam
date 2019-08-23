# Generated by Django 2.2.4 on 2019-08-21 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Cm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Eco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloq_calcio', models.CharField(default=None, max_length=300, null=True)),
                ('nitrato', models.CharField(default=None, max_length=300, null=True)),
                ('estamina', models.CharField(default=None, max_length=300, null=True)),
                ('bra', models.CharField(default=None, max_length=300, null=True)),
                ('ieca', models.CharField(default=None, max_length=300, null=True)),
                ('clopido', models.CharField(default=None, max_length=300, null=True)),
                ('aas', models.CharField(default=None, max_length=300, null=True)),
                ('b_bloqueador', models.CharField(default=None, max_length=300, null=True)),
                ('diuretico', models.CharField(default=None, max_length=300, null=True)),
                ('others', models.CharField(default=None, max_length=300, null=True)),
                ('cat', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Cat')),
                ('cm', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Cm')),
                ('eco', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Eco')),
            ],
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None, null=True)),
                ('time', models.TimeField(null=True)),
                ('time_observation', models.CharField(default=None, max_length=300, null=True)),
                ('protocol', models.BooleanField(default=False)),
                ('protocol_justify', models.CharField(default=None, max_length=300, null=True)),
                ('restraint', models.BooleanField(default=False)),
                ('capture_movement', models.BooleanField(default=False)),
                ('extravasation', models.BooleanField(default=False)),
                ('exam_observations', models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ImageProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Motivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='StressProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Te',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Radiofarmaco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(null=True)),
                ('dose', models.CharField(default=None, max_length=50, null=True)),
                ('material', models.CharField(default=None, max_length=100, null=True)),
                ('adm', models.CharField(default=None, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='images/%Y/%m/%d/')),
                ('stress_detail', models.CharField(default=None, max_length=200, null=True)),
                ('prescription', models.TextField(default=None, null=True)),
                ('image_protocol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.ImageProtocol')),
                ('stress_protocol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.StressProtocol')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('cpf', models.CharField(default=None, max_length=11, null=True)),
                ('mobile', models.CharField(default=None, max_length=18, null=True)),
                ('crm', models.CharField(default=None, max_length=18, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_data', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('email', models.CharField(default=None, max_length=100, null=True)),
                ('birthday', models.DateField(default=None, null=True)),
                ('height', models.CharField(default=None, max_length=100, null=True)),
                ('weight', models.CharField(default=None, max_length=100, null=True)),
                ('sex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Sex')),
            ],
        ),
        migrations.CreateModel(
            name='Hpp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=15)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Level')),
            ],
        ),
        migrations.CreateModel(
            name='ExamMotivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Exam')),
                ('motivation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Motivation')),
            ],
        ),
        migrations.CreateModel(
            name='ExamHpp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Exam')),
                ('hpp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Hpp')),
            ],
        ),
        migrations.CreateModel(
            name='ExamHda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Exam')),
                ('hda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Hda')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Patient'),
        ),
        migrations.AddField(
            model_name='exam',
            name='rest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='radio2', to='dashboard.Radiofarmaco'),
        ),
        migrations.AddField(
            model_name='exam',
            name='rest_examination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exm2', to='dashboard.Examination'),
        ),
        migrations.AddField(
            model_name='exam',
            name='stress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='radio1', to='dashboard.Radiofarmaco'),
        ),
        migrations.AddField(
            model_name='exam',
            name='stress_examination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exm1', to='dashboard.Examination'),
        ),
        migrations.AddField(
            model_name='exam',
            name='te',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Te'),
        ),
    ]
