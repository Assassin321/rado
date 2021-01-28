from django.db import models


# Create your models here.
class RadoBoat(models.Model):
    rid = models.CharField(primary_key=True, max_length=100)
    bid = models.CharField(default="NULL", max_length=100)


class RadoData(models.Model):
    radoData = models.ImageField(default="radoImages/default.jpg", upload_to="Images/%Y/%m/%d/")
    rid = models.ForeignKey(RadoBoat, on_delete=models.CASCADE, max_length=100)
    UpdateTime = models.DateTimeField(auto_now_add=True)


class SeaRank(models.Model):
    rid = models.ForeignKey(RadoBoat, on_delete=models.CASCADE, max_length=100)
    rank = models.CharField(default="NULL", max_length=100)
    RankTime = models.DateTimeField(auto_now_add=True)


class RecognizeInfo(models.Model):
    rid = models.ForeignKey(RadoBoat, on_delete=models.CASCADE, max_length=100)
    seaInfo = models.TextField(default="NULL")
    Time = models.DateTimeField(auto_now_add=True)


class BoatRecord(models.Model):
    bid = models.CharField(default="NULL", max_length=100)
    x = models.CharField(default="NULL", max_length=100)
    y = models.CharField(default="NULL", max_length=100)
    BoatTime = models.DateTimeField(auto_now_add=True)
