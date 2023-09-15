from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register('labs', views.LabViewSet, basename='labs')
router.register('tests', views.TestViewSet)
router.register('indicators', views.IndicatorViewSet)
router.register('metrics', views.MetricViewSet)
router.register('indicator_metrics', views.IndicatorMetricViewSet)
router.register('scores', views.ScoreViewSet)
router.register('references', views.ReferenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('result-test/<uuid:test_id>/', views.ResultTestAPIView.as_view(), name='result-test'),

]
