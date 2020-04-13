from datetime import datetime
import os
import django
import csv

os.environ['DJANGO_SETTINGS_MODULE'] = "django_api.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_api.settings")
django.setup()

from django_api.models import PerformanceMetrics

dataReader = csv.reader(open('dataset.csv'), delimiter=',', quotechar='"')

for row in dataReader:
    data = PerformanceMetrics()

    entry_date = datetime.strptime(row[0], "%Y-%m-%d").date()
    data.date = entry_date
    data.channel = row[1]
    data.country = row[2]
    data.os = row[3]
    data.impressions = row[4]
    data.clicks = row[5]
    data.installs = row[6]
    data.spend = row[7]
    data.revenue = row[8]

    data.save()
