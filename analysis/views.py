from django.views.generic import FormView
from django.urls import reverse_lazy
from . import forms as analysis_forms


class ChartView(FormView):
    form_class = analysis_forms.ChartForm
    success_url = reverse_lazy('success')
    template_name = 'analysis/chart.html'