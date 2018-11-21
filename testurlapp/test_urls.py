from django.urls import re_path
from testurlapp import views

urlpatterns = [
    re_path(r'^user/(\d{2})/(\d{4})', views.home, name='home'),
]