from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class DemoView(LoginRequiredMixin, TemplateView):
    template_name = "demo.html"
