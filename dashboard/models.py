from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user_data')
    created = models.DateTimeField(editable=False, default=timezone.now)

    # Personal data
    name = models.CharField(max_length=100, null=True, default=None)
    cpf = models.CharField(max_length=11, null=True, default=None)
    mobile = models.CharField(max_length=18, null=True, default=None)
    crm = models.CharField(max_length=18, null=True, default=None)
    receive_email = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - ' + self.crm

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(Profile, self).save(*args, **kwargs)

    def create_account(**kwargs):
        with transaction.atomic():

            user = User.objects.create_user(
                username=kwargs['email'],
                first_name=kwargs['first_name'],
                last_name="",
                password=kwargs['password'],
                email=kwargs['email']
            )
            profile = Profile(
                user=user,
                cpf=kwargs['cpf'],
                name=kwargs['name'],
                mobile=kwargs['mobile'] if 'mobile' in kwargs else None,        
                crm=kwargs['crm'] if 'crm' in kwargs else None,
                receive_email=kwargs['crm'] if 'crm' in kwargs else False,

            )
            profile.save()
        return profile

    def update_account(**kwargs):
        with transaction.atomic():

            profile = Profile.objects.get(cpf=kwargs['cpf'])
            profile.cpf = kwargs['cpf']
            profile.mobile = kwargs['mobile'] if 'mobile' in kwargs else None
            profile.crm=kwargs['crm'] if 'crm' in kwargs else None
            profile.receive_email=kwargs['crm'] if 'crm' in kwargs else False
            profile.user.first_name = kwargs['first_name']
            profile.user.last_name = kwargs['last_name']
            profile.user.email = kwargs['email']
            profile.user.save()
            profile.save()
        return profile


class Sex(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100, null=True, default=None)
    email = models.CharField(max_length=100, null=True, default=None)
    cpf = models.CharField(max_length=11, null=True, default=None)
    birthday = models.DateField(null=True, default=None)
    height = models.CharField(max_length=100, null=True, default=None)
    weight = models.CharField(max_length=100, null=True, default=None)
    sex = models.ForeignKey('Sex',
                            on_delete=models.CASCADE)

    def __str__(self):
        if(self.cpf):
            return self.cpf + " - " + self.name

        return "--- - " + self.name


class Radiofarmaco(models.Model):
    time = models.TimeField(null=True)
    dose = models.CharField(max_length=50, null=True, default=None)
    material = models.CharField(max_length=100, null=True, default=None)
    adm = models.CharField(max_length=200, null=True, default=None)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', default=None,
                              blank=True, null=True)
    image_protocol = models.ForeignKey('ImageProtocol',
                                       on_delete=models.CASCADE)
    stress_protocol = models.ForeignKey('StressProtocol',
                                        on_delete=models.CASCADE)
    stress_detail = models.CharField(max_length=200, null=True, default=None)
    prescription = models.TextField(null=True, default=None)


class Examination(models.Model):
    date = models.DateField(null=True, default=None)
    time = models.TimeField(null=True)
    time_observation = models.CharField(max_length=300, null=True, default=None)
    protocol = models.BooleanField(default=False)
    protocol_justify = models.CharField(max_length=300, null=True, default=None)
    restraint = models.BooleanField(default=False)
    capture_movement = models.BooleanField(default=False)
    extravasation = models.BooleanField(default=False)
    exam_observations = models.TextField(null=True, default=None)


class Eco(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Te(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Cm(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Exam(models.Model):
    patient = models.ForeignKey('Patient',
                                on_delete=models.CASCADE)
    # estresse
    stress = models.ForeignKey('Radiofarmaco',
                                on_delete=models.CASCADE,
                                related_name="radio1")

    stress_examination = models.ForeignKey('Examination',
                                           on_delete=models.CASCADE,
                                           related_name="exm1")

    #repouso
    rest = models.ForeignKey('Radiofarmaco',
                             on_delete=models.CASCADE,
                             related_name="radio2")

    rest_examination = models.ForeignKey('Examination',
                                         on_delete=models.CASCADE,
                                         related_name="exm2")

    # medicamentos
    bloq_calcio = models.CharField(max_length=300, null=True, default=None)
    nitrato = models.CharField(max_length=300, null=True, default=None)
    estamina = models.CharField(max_length=300, null=True, default=None)
    bra = models.CharField(max_length=300, null=True, default=None)
    ieca = models.CharField(max_length=300, null=True, default=None)
    clopido = models.CharField(max_length=300, null=True, default=None)
    aas = models.CharField(max_length=300, null=True, default=None)
    b_bloqueador = models.CharField(max_length=300, null=True, default=None)
    diuretico = models.CharField(max_length=300, null=True, default=None)
    others = models.CharField(max_length=300, null=True, default=None)

    # exames previos
    eco = models.ForeignKey('Eco',
                             on_delete=models.CASCADE,
                             null=True,
                             default=None)
    te = models.ForeignKey('Te',
                           on_delete=models.CASCADE,
                           null=True,
                           default=None)
    cat = models.ForeignKey('Cat',
                            on_delete=models.CASCADE,
                            null=True,
                            default=None)
    cm = models.ForeignKey('Cm',
                           on_delete=models.CASCADE,
                           null=True,
                           default=None)
    

class ImageProtocol(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class StressProtocol(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Motivation(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class ExamMotivation(models.Model):
    exam = models.ForeignKey('Exam',
                              on_delete=models.CASCADE)
    motivation = models.ForeignKey('Motivation',
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.exam.patient.name + " - " + self.motivation.name



class Hda(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class ExamHda(models.Model):
    exam = models.ForeignKey('Exam',
                              on_delete=models.CASCADE)
    hda = models.ForeignKey('Hda',
                            on_delete=models.CASCADE)

    def __str__(self):
        return self.exam.patient.name + " - " + self.hda.name


class Level(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Hpp(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=15)
    level = models.ForeignKey('Level',
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ExamHpp(models.Model):
    exam = models.ForeignKey('Exam',
                              on_delete=models.CASCADE)
    hpp = models.ForeignKey('Hpp',
                            on_delete=models.CASCADE)

    def __str__(self):
        return self.exam.patient.name + " - " + self.hpp.name


