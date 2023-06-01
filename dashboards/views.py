from django.shortcuts import render
from django.views import generic


# render blank dashboard.
class BlankDashboardView(generic.TemplateView):
    template_name = 'dashboards/blank-dashboard.html.twig'


# render original dashboard.
class OriginalDashboardView(generic.TemplateView):
    template_name = 'dashboards/original-dashboard.html.twig'



