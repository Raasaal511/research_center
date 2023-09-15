from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Lab, Test, Indicator, Metric, IndicatorMetric, Score, Reference

from .serializers import (LabSerializer, TestSerializer, IndicatorSerializer,
                          MetricSerializer, IndicatorMetricSerializer,
                          ScoreSerializer, ReferenceSerializer)


class LabViewSet(viewsets.ModelViewSet):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class IndicatorViewSet(viewsets.ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer


class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer


class IndicatorMetricViewSet(viewsets.ModelViewSet):
    queryset = IndicatorMetric.objects.all()
    serializer_class = IndicatorMetricSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer


class ResultTestAPIView(APIView):

    def get(self, request, test_id):
        test = Test.objects.get(id=test_id)
        duration = test.duration_seconds()
        scores = test.score_set.all()
        results = []

        for score in scores:
            indicator_metric = score.indicator_metric
            referense = Reference.objects.get(indicator_metric=indicator_metric.id, is_active=True)
            is_within_normal_range = True if referense.min_score <= score.score <= referense.max_score else False

            results.append({
                "id": score.id,
                "score": score.score,
                "indicator_name": indicator_metric.indicator.name,
                "metric_name": indicator_metric.metric.name,
                "metric_unit": indicator_metric.metric.unit,
                "is_within_normal_range": is_within_normal_range
            })

        test_results = {
            'id': test.id,
            'lab_id': test.lab.id,
            'duration_seconds': duration,
            'results': results,
        }

        return Response(test_results)
