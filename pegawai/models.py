from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class PegawaiManager(BaseUserManager):
    def create_user(self, nip, password=None):
        if not nip:
            raise ValueError("NIP harus diisi")
        user = self.model(nip=nip)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nip, password=None):
        user = self.create_user(nip, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Pegawai(AbstractBaseUser):
    nip = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='foto_pegawai/', blank=True, null=True)

    golongan = models.CharField(max_length=50, blank=True, null=True)
    pangkat = models.CharField(max_length=50, blank=True, null=True)
    pendidikan = models.CharField(max_length=100, blank=True, null=True)
    tim_kerja = models.CharField(max_length=100, blank=True, null=True)
    tmt = models.CharField(blank=True, null=True)
    angker_2024 = models.CharField(max_length=10, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    ...


    objects = PegawaiManager()

    USERNAME_FIELD = 'nip'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.nip} - {self.nama}"

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class BackgroundSetting(models.Model):
    background = models.ImageField(upload_to='backgrounds/')

    def __str__(self):
        return self.background.name
