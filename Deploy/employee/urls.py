from django.conf.urls import url
from employee import views

urlpatterns = [
    url('train', views.train, name='train'),
]
