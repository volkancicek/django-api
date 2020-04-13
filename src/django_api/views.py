from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import FloatField, Sum, F

from .serializers import PerformanceMetricsSerializer
from .models import PerformanceMetrics


class PerformanceMetricsView(ListAPIView):
    serializer_class = PerformanceMetricsSerializer
    queryset = PerformanceMetrics.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filter_fields = ('date', 'channel', 'country', 'os')
    ordering_fields = '__all__'

    def get_queryset(self):
        """
        List of dictionaries containing field name as key and value as their values
        """

        aggregation_field = ('impressions', 'clicks', 'installs', 'spend', 'revenue', 'cpi')

        queryset = PerformanceMetrics.objects.all()
        query_params = self.request.query_params
        group_by = query_params.get("group_by")
        date_from = query_params.get("date_from")
        date_to = query_params.get("date_to")
        fields = query_params.get("fields", '')
        if fields == '*':
            fields = (
            'date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue', 'cpi')
        else:
            fields = fields.split(',') if fields != '' else []

        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)

        if group_by:
            group_by = group_by.split(',')
            for field in fields:
                if field not in group_by and field not in aggregation_field:
                    group_by.append(field)
            queryset = queryset.values(*group_by).annotate(impressions=Sum('impressions'), clicks=Sum('clicks'),
                                                           installs=Sum('installs', output_field=FloatField()),
                                                           spend=Sum('spend', output_field=FloatField()),
                                                           revenue=Sum('revenue')).annotate(
                cpi=F('spend') / F('installs'))

        return queryset
