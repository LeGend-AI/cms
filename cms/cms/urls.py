from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path(r'members/', include('members.urls')),
    path(r'', TemplateView.as_view(template_name="index.html")),
    path(r'about', TemplateView.as_view(template_name="about.html")),
    path('accounts/', include('django.contrib.auth.urls')),
]
