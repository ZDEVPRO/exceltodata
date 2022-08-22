from django.db import models


class ExeltoData(models.Model):
    DATE = models.CharField(max_length=600, blank=True)
    INN = models.CharField(max_length=600)
    FIRMA = models.CharField(max_length=600)
    SUMDA = models.CharField(max_length=600, blank=True)
    KURS = models.CharField(max_length=600, blank=True)
    DOLLAR = models.CharField(max_length=600, blank=True)
    ID = models.AutoField(primary_key=True)
    CLIENT = models.CharField(max_length=600, blank=True)
    REGION = models.CharField(max_length=600, blank=True)
    MANAGER = models.CharField(max_length=600, blank=True)

    def __str__(self):
        return self.FIRMA

    class Meta:
        verbose_name = 'Exel To Data'
        verbose_name_plural = 'Exel To Data'


class AllData(models.Model):
    ID = models.AutoField(primary_key=True)
    DATE = models.CharField(max_length=601, blank=True)
    INN = models.CharField(max_length=600)
    FIRMA = models.CharField(max_length=600)
    SUMDA = models.CharField(max_length=600, blank=True)
    KURS = models.CharField(max_length=600, blank=True)
    DOLLAR = models.CharField(max_length=600, blank=True)
    CLIENT = models.CharField(max_length=600, blank=True)
    REGION = models.CharField(max_length=600, blank=True)
    MANAGER = models.CharField(max_length=600, blank=True)

    def __str__(self):
        return self.FIRMA

    class Meta:
        verbose_name = 'All Data'
        verbose_name_plural = 'All Data'
