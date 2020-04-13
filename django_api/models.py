from django.db import models


class PerformanceMetrics(models.Model):
    date = models.DateField(blank=True, null=True)
    channel = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    os = models.CharField(max_length=255, null=True)
    impressions = models.IntegerField(null=True)
    clicks = models.IntegerField(null=True)
    installs = models.IntegerField(null=True)
    spend = models.FloatField(null=True)
    revenue = models.FloatField(null=True)

    @property
    def cpi(self):
        return self.spend / self.installs
