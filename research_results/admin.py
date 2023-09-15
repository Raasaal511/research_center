from django.contrib import admin

from .models import Lab, Test, Indicator, Metric, IndicatorMetric, Score, Reference


class LabAdmin(admin.ModelAdmin):
    pass


class TestAdmin(admin.ModelAdmin):
    pass


class IndicatorAdmin(admin.ModelAdmin):
    pass


class MetricAdmin(admin.ModelAdmin):
    pass


class IndicatorMetricAdmin(admin.ModelAdmin):
    pass


class ScoreAdmin(admin.ModelAdmin):
    pass


class ReferenceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lab, LabAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(Metric, MetricAdmin)
admin.site.register(IndicatorMetric, IndicatorMetricAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Reference, ReferenceAdmin)
