from django.db import models

class Ariza(models.Model):
    ism = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    yosh = models.CharField(max_length=50, blank=True, null=True)
    shahar = models.CharField(max_length=100, blank=True, null=True)
    yozilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism

class Savol(models.Model):
    ism = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    savol_matni = models.TextField()
    yozilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism

class Kurs(models.Model):
    nomi = models.CharField(max_length=200)
    haqida = models.TextField()

    def __str__(self):
        return self.nomi

class Natija(models.Model):
    oquvchi_ismi = models.CharField(max_length=100)
    fikri = models.TextField()
    rasm = models.ImageField(upload_to='natijalar/', blank=True, null=True)

    def __str__(self):
        return self.oquvchi_ismi

class SavolJavob(models.Model):
    savol = models.CharField(max_length=255)
    javob = models.TextField()

    def __str__(self):
        return self.savol