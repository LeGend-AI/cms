from django.urls import path, include, reverse_lazy
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    path(r'members/', include('members.urls')),
    path(r'', TemplateView.as_view(template_name="index.html"), name='index'),
    path(r'about', TemplateView.as_view(template_name="about.html"), name='about'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
