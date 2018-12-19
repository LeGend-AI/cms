from django.urls import path, include

urlpatterns = [
    path(r'/^member/', include('members.urls')),
    path(r'/', include('members.urls')),
    path(r'/about', include('members.urls')),
]
