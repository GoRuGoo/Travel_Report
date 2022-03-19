from django.db import models

# Create your models here.
from accounts.models import CustomUser

class TravelReport(models.Model):
    user = models.ForeignKey(CustomUser,verbose_name='ユーザー名',on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル',max_length=40)
    date = models.DateTimeField(verbose_name='旅行日時',auto_now=True)
    transportation = models.CharField(verbose_name='交通手段',max_length=20)
    cost = models.IntegerField(default=100)
    member = models.CharField(verbose_name='メンバー',max_length=30)
    thoughts = models.TextField(verbose_name='概要',blank=True)

    def __str__(self):
        return self.title