from django.urls import path

from . import views

app_name = "members"

urlpatterns = [
  path('/^members', views.MemberListView.as_view(), name='list'),
  path('/^sign_up', views.SignUpView.as_view(), name='sign_up'),
]
